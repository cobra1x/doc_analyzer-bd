from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from app.core.llm import get_embeddings
from typing import Optional

ai_history=[]

vector_store: Optional[InMemoryVectorStore] = None

def add_store(path):
    global vector_store
    global ai_history

    loader=PyPDFLoader(path)
    pages=loader.load()


    splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
    chunks=splitter.split_documents(pages)
    vector_store=InMemoryVectorStore.from_documents(
        documents=chunks,
        embedding=get_embeddings()
    )
    ai_history=[]

def get_retriever():
    global vector_store
    if vector_store is None:
        raise ValueError("Vector store is not loaded. Please upload a document first.")

    return vector_store.as_retriever()