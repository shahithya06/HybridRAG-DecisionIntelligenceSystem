import chromadb
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ✅ Use PersistentClient (NEW way)
chroma_client = chromadb.PersistentClient(path="./chroma_db")

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = chroma_client.get_or_create_collection(
    name="business_docs",
    embedding_function=embedding_function
)


def load_documents():
    with open("data/sales_reports.txt", "r", encoding="utf-8") as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            ids=[f"doc_{i}"]
        )

    print("✅ Documents loaded into Chroma")


def query_vector(question):
    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    return results["documents"][0]