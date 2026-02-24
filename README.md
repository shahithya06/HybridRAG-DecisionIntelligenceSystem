📊 Business Hybrid RAG System
Vector RAG + Graph RAG + Hybrid RAG using Neo4j, Chroma & Groq
🚀 Project Overview

This project implements three Retrieval-Augmented Generation (RAG) architectures:

🔹 Vector RAG (ChromaDB)

🔹 Graph RAG (Neo4j Knowledge Graph)

🔹 🔥 Hybrid RAG (Vector + Graph combined)

The system acts as a Business Report & Decision Assistant, capable of analyzing structured and unstructured data to generate strategic insights with source transparency.

🧠 Architecture
User Question
        ↓
Streamlit Interface
        ↓
Hybrid Orchestration (Python)
        ↓
 ┌────────────────────────────┐
 │                            │
 │  Chroma Vector Retrieval   │
 │  (Unstructured Documents)  │
 │                            │
 └────────────────────────────┘
                +
 ┌────────────────────────────┐
 │                            │
 │   Neo4j Knowledge Graph    │
 │   (Structured Relations)   │
 │                            │
 └────────────────────────────┘
        ↓
Groq LLM (Reasoning Layer)
        ↓
Answer + Source Attribution
🏗 Tech Stack
Component	Technology
LLM	Groq (Llama 3.3 70B Versatile)
Graph Database	Neo4j
Vector Database	ChromaDB
Embeddings	sentence-transformers (all-MiniLM-L6-v2)
Backend	Python
UI	Streamlit
Environment	VSCode
📂 Project Structure
business-hybrid-rag/
│
├── app.py                 # Streamlit application
├── graph.py               # Neo4j graph setup & queries
├── vector_store.py        # Chroma vector setup & retrieval
├── init_graph.py          # Initialize graph + load documents
│
├── data/
│   ├── sales_reports.txt
│   ├── meeting_notes.txt
│   └── feedback.txt
│
├── chroma_db/             # Persistent vector database
├── .env                   # Environment variables
└── README.md
📊 Dataset Description
📄 sales_reports.txt

Contains:

Regional revenue performance

Product decline analysis

Competitive impact

Marketing & supply chain insights

📝 meeting_notes.txt

Contains:

Strategy discussions

Manager accountability

Budget decisions

Proposed corrective actions

💬 feedback.txt

Contains:

Customer complaints

Satisfaction drop

Delivery issues

Product reliability concerns

🔐 Environment Setup

Create a .env file in project root:

GROQ_API_KEY=your_groq_key
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password

Install dependencies:

pip install streamlit neo4j chromadb groq python-dotenv sentence-transformers langchain-text-splitters
⚙️ Setup Instructions
1️⃣ Initialize Graph + Vector DB
python init_graph.py

This will:

Populate Neo4j with business relationships

Load documents into ChromaDB

2️⃣ Run Application
streamlit run app.py

Open:

http://localhost:8501
🔥 Example Hybrid Questions

Try:

Why did Laptop sales decline in the South region and what actions should the responsible manager take?

Identify the manager responsible for the underperforming product and suggest a recovery strategy.

Analyze South region performance using reports and structured relationships.

🧩 How Hybrid RAG Works Here
🔹 Vector RAG

Retrieves:

Sales decline causes

Customer complaints

Marketing reductions

🔹 Graph RAG

Retrieves:

Product → Region

Region → Manager

Product → Category

🔹 Hybrid RAG

LLM combines:

Semantic insights (vector)

Structured accountability (graph)

Strategic recommendations

📚 Source Attribution

The system prints:

Vector document chunks used

Graph records retrieved

Ensuring transparency in generated answers.

💼 Resume Value

This project demonstrates:

Multi-database retrieval orchestration

Knowledge graph integration

Hybrid reasoning architecture

LLM production integration

Debugging of real-world API issues

Environment management & deployment readiness

🎯 Key Learnings

Difference between Vector vs Graph retrieval

Why Hybrid RAG improves reasoning quality

Managing model deprecations (Groq)

Handling embedding & persistence issues

Structured + unstructured data fusion

🔮 Future Improvements

Intelligent retrieval routing

Dynamic Cypher generation via LLM

Evaluation metrics for answer quality

Confidence scoring

Deployment on cloud

🏁 Conclusion

This project showcases a complete Hybrid RAG implementation combining:

Knowledge Graph reasoning

Semantic search

LLM-driven insight synthesis


Built entirely in VSCode using Python, Neo4j, Chroma, and Groq.
