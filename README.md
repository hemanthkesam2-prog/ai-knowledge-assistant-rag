# AI Knowledge Assistant

An AI-powered knowledge assistant that uses Retrieval-Augmented Generation (RAG) to answer questions from uploaded knowledge sources.

## Features

- Document-based question answering
- Retrieval-Augmented Generation (RAG)
- Document chunking and embeddings
- Semantic similarity search
- ChromaDB vector database
- LLM-powered responses
- Context-aware answers

## Tech Stack

- Python
- ChromaDB
- Sentence Transformers
- RAG
- Large Language Models (LLMs)
- Git & GitHub

## Project Files

- main.py — Main application
- rag.py — RAG and ChromaDB functionality
- file.txt — Knowledge/source file
- requirements.txt — Required Python packages

## How It Works

1. Knowledge is loaded from the source file.
2. Documents are processed and divided into chunks.
3. Embeddings are generated for the chunks.
4. Embeddings are stored in ChromaDB.
5. User questions are converted into embeddings.
6. Relevant information is retrieved using semantic similarity search.
7. The retrieved context is used to generate the answer.

## Installation

```bash
pip install -r requirements.txt
