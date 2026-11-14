# Enterprise Knowledge Assistant – RAG

An AI-powered Enterprise Knowledge Assistant that helps users retrieve accurate and contextually relevant information from enterprise documents using Retrieval-Augmented Generation (RAG).

## 📌 Project Overview

The Enterprise Knowledge Assistant is designed to simplify access to organizational knowledge by allowing users to ask questions in natural language and receive relevant, context-aware responses.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a knowledge base and generate answers using Azure OpenAI.

Instead of relying solely on the knowledge stored in an LLM, the application retrieves relevant document content and uses it as context to generate more accurate and meaningful responses.

## 🎯 Objectives

- Build an intelligent enterprise document-based question-answering system.
- Retrieve relevant information using vector similarity search.
- Generate context-aware responses using Azure OpenAI.
- Reduce manual effort in searching through enterprise documents.
- Integrate MCP to support standardized communication between AI applications and external tools.

## 🏗️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| LangChain | RAG application orchestration |
| Azure OpenAI | LLM-based response generation and embeddings |
| FAISS | Vector storage and similarity search |
| MCP | Model Context Protocol integration |
| Streamlit | User interface (if configured) |

## ⚙️ System Architecture

The application follows a Retrieval-Augmented Generation architecture.

1. **Document Loading:** Enterprise documents are loaded into the application.
2. **Text Chunking:** Documents are divided into smaller chunks for efficient retrieval.
3. **Embedding Generation:** Text chunks are converted into numerical vector representations.
4. **Vector Storage:** Embeddings are stored in the FAISS vector database.
5. **User Query:** The user submits a question through the application.
6. **Similarity Search:** FAISS retrieves the most relevant document chunks.
7. **Context Augmentation:** Retrieved information is provided as context to Azure OpenAI.
8. **Response Generation:** Azure OpenAI generates a context-aware answer.
9. **MCP Integration:** MCP provides a standardized mechanism for connecting AI applications with external tools and resources.

## 📂 Project Structure

```text
Knowledge_enterprise_rag/
│
├── data/                   # Enterprise knowledge documents
│
├── src/                    # Application source code
│
├── tests/                  # Test cases
│
├── vectorstore/
│   └── faiss_index/        # FAISS vector index
│
├── .gitignore              # Git ignored files
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Knowledge_enterprise_rag
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root and configure your Azure OpenAI credentials.

```env
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_API_VERSION=your_api_version
AZURE_OPENAI_DEPLOYMENT=your_deployment_name
```

Use the actual variable names expected by your application.

**Important:** Never upload API keys, passwords, or other credentials to GitHub.

## ▶️ Running the Application

Run the application using its configured entry point.

For example, if the application uses Streamlit:

```bash
streamlit run src/app.py
```

Replace the entry point with the actual application file in your project.

## 🔍 Key Features

- Natural language question answering.
- Document-based information retrieval.
- Semantic search using vector embeddings.
- Context-aware response generation.
- FAISS-based vector similarity search.
- Azure OpenAI integration.
- MCP-based tool and resource integration.

## 🔐 Security Considerations

- API credentials are maintained using environment variables.
- Sensitive configuration files are excluded through `.gitignore`.
- Virtual environments are excluded from version control.
- Access to enterprise information should follow organizational security policies.

## 🔮 Future Enhancements

- Support for additional document formats.
- Improved document retrieval and ranking.
- User authentication and role-based access control.
- Conversation history and memory.
- Advanced monitoring and evaluation of generated responses.
- Cloud deployment and scalability improvements.

## 👩‍💻 Contributors

Developed as a collaborative team project.

**Project:** Enterprise Knowledge Assistant – RAG

**Core Technologies:** Python | Azure OpenAI | LangChain | FAISS | MCP

---

*Building smarter enterprise knowledge access through Retrieval-Augmented Generation.*
