import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
from graph import query_graph
from vector_store import query_vector

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="Hybrid Business RAG")
st.title("📊 Business Report & Decision Assistant")

question = st.text_input("Ask your business question:")

if question:

    vector_results = query_vector(question)
    graph_results = query_graph()

    context = f"""
    BUSINESS REPORT DATA:
    {vector_results}

    KNOWLEDGE GRAPH DATA:
    {graph_results}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert business analyst."},
            {"role": "user", "content": f"{context}\n\nQuestion: {question}"}
        ]
    )

    answer = response.choices[0].message.content

    st.subheader("📌 Final Answer")
    st.write(answer)

    st.divider()

    st.subheader("📚 Sources Used")

    st.write("🔹 Vector Sources:")
    for doc in vector_results:
        st.write("-", doc[:200])

    st.write("🔹 Graph Sources:")
    for record in graph_results:
        st.write("-", record)