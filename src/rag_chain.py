
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

INDEX_DIR = "vectorstore/faiss_index"

# Load the embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

# Load the saved FAISS index
vectorstore = FAISS.load_local(
    INDEX_DIR,
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# Configure the local LLM
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://localhost:11434"
)

prompt = ChatPromptTemplate.from_template("""
You are an Enterprise Knowledge Assistant.

Answer the question using ONLY the context below.
If the answer is not present in the context, say:
"I could not find this information in the available documents."

Context:
{context}

Question:
{question}

Answer:
""")

def ask_question(question: str) -> dict:
    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    response = llm.invoke(
        prompt.format_messages(
            context=context,
            question=question
        )
    )

    sources = list(dict.fromkeys(
        doc.metadata.get("source", "Unknown")
        for doc in docs
    ))

    return {
        "answer": response.content,
        "sources": sources
    }


if __name__ == "__main__":
    question = input("Ask a company policy question: ")
    result = ask_question(question)

    print("\nAnswer:")
    print(result["answer"])

    print("\nSources:")
    for source in result["sources"]:
        print(source)
