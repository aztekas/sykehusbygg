import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "FAISS is a library for efficient similarity search on dense vectors."
# text = "The self-replicating micro-organisms were unbelievably resilient, even in sub-zero environments."
# text = "Sykehusbygg har flere rom, blant annet Sengerom, intermediær, SR.134.08 og Ammerom, SR.003.00"
tokens = enc.encode(text)

# Show both ID and the decoded string for each token
for token in tokens:
    print(f"{token:>6}  {enc.decode([token])!r}")

print(f"\nTotal tokens: {len(tokens)}")
