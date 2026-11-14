
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

DATA_DIR = Path("data")
INDEX_DIR = "vectorstore/faiss_index"

documents = []

for file in DATA_DIR.glob("*.txt"):
    documents.extend(
        TextLoader(str(file), encoding="utf-8").load()
    )

if not documents:
    raise ValueError("No .txt files found in the data folder.")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local(INDEX_DIR)

print(f"Success! Indexed {len(chunks)} document chunks.")
