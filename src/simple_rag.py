
from langchain_community.document_loaders import SitemapLoader
from langchain_community.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import trafilatura

ROOT = "https://kunnskapsbanken.sykehusbygg.no"
DEPTH = 2

def trafilatura_extractor(html: str) -> str:
    return trafilatura.extract(html) or ""

print(f"Loading pages with depth={DEPTH} from {ROOT}")
# loader = SitemapLoader(web_path=f"{ROOT}/sitemap.xml")
loader = RecursiveUrlLoader(
    url=ROOT,
    max_depth=DEPTH,                 # increase for deeper subpages
    use_async=True,
    extractor=trafilatura_extractor,     # robust HTML->text
    prevent_outside=True,        # stay under ROOT
    timeout=30,
)

docs = loader.load()

attachment_docs = []
for doc in docs:
    # crude link collection
    for link in doc.metadata.get("links", []):
        if link.lower().endswith((".pdf", ".docx", ".doc")):
            print(link)
        else:
            print(" -> empty links")
            # attachment_docs.extend(load_attachment(link))

print(f"Number of docs: {len(docs)}")

print("Chuncking")
# --- Chunking ---
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

print("Build vector store")
# --- Vector store ---
emb = OpenAIEmbeddings()
vs = FAISS.from_documents(chunks, emb)
retriever = vs.as_retriever(k=5)

# --- Prompt + chain ---
prompt = PromptTemplate.from_template(
    "Answer concisely using ONLY the context. If missing, say you don't know.\n"
    "Context:\n{context}\n\nQuestion: {question}\nAnswer:"
)

def join_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

print("Create RAG")
llm = ChatOpenAI(model="gpt-4o-mini")
rag = (
    {"context": retriever | join_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("Query")
# --- Query ---
print(rag.invoke("Hva kan man finne i veilederen for tidligfasen i sykehusbyggprosjekter?"))
