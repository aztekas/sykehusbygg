# RAG Tutorial

A collection of concepts needed to understand RAG

_This is not an extensive tutorial, you will need to read the code and ask Google or GPT whenever you're stuck_


## 01 - Tokens

What is a token, and how many characters is in one token (not an exact science)

- [Text to tokens](01_text_to_tokens.py)
- [Comparison of tokenizers for different models](01b_difference_token_models.py)

## 02 - Vector Store

What is FAISS, and how does a vector store work.

You start with vectors, then convert it to an index with FAISS, then you can create a new vector and use FAISS to figure out which are closest (k determines how many to find)

- [Simple vector store](02_vector_store.py)


## 03 - Chunks

Input text needs to be in suitable chunks. Sweet spot is around 4-500 tokens.

The standard way is to split the text in chunks, and include overlap, so that context is not lost.

An alternative is semantic chunks, where the text is split in a "smart" way, where each chunk makes sense.

A third option is a combination, with semantic chunks that also overlap in the resulting chunks sent to the LLM.

In the [simple rag example](10_simple_rag.py), the chunks are created simply by splitting and using overlap

## 04 - Embedder

An embedder converts each chunk tokens, and then to a vector of fixed size (these are quite long, depending on model).

The result is an array of vectors, i.e. the vector store. Just like in the [vector store example](02_vector_store.py)

## 05 - Prompt

The promt is constructed in a suitable way, like in the [simple rag example](10_simple_rag.py)

**(Not sure from here)**


# Next steps

## 2025-11-04

### Chunks

How do we construct the chunks?

It seems like it is better to construct a more readable text instead of jsons. It seems like the LLM likes it better, just as humans, but this should be double checked.

Theory:

Instead of JSON:
```
{
    "room": "Big",
    "electricity": "Yes",
}
```

Use more simple text:
```
Room: Big
Electricity: Yes
```

Should we construct logic chunks from the spreadsheet, i.e. convert each json array element into text?

Or, is that too big, and we should use smaller ones?

### Promt

How do we best create the prompt?

