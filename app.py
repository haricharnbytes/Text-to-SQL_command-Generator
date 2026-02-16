
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("GROQ_API_KEY not found in environment variables.")
    st.stop()

# -----------------------------
# Initialize the LLM
# -----------------------------
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3
)

# -----------------------------
# Streamlit App
# -----------------------------
st.set_page_config(page_title="Database QA Assistant", page_icon="🧠")
st.title("🧠 Database QA Assistant")
st.markdown("""
Ask questions about your database schema and get precise, structured answers.
""")

# Input box for user question
question = st.text_area("💬 Ask your question:", height=150)

# Run button
if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question before submitting.")
    else:
        # -----------------------------
        # Build the prompt
        # -----------------------------
        prompt = ChatPromptTemplate.from_template("""
Role: You are an expert-level AI assistant with strong knowledge of databases, data modeling, and query logic.

Objective: Analyze the database structure provided in the user’s question and generate answers that are accurate, structured, and directly based on that structure.

Instructions:

Extract and Understand the Database Structure

Carefully read the database schema, table names, column names, relationships, and constraints provided in the question.

Use this information as the foundation for your answers.

Answer Using the Database Context

Write queries, explanations, or calculations strictly based on the given schema.

Avoid assuming fields, relationships, or data types that are not provided.

Include table and column references explicitly where relevant.

Structure and Clarity

Organize answers with headings, bullet points, or numbered lists where appropriate.

Provide step-by-step reasoning for queries, joins, or calculations derived from the schema.

Label query outputs or logical steps clearly for easy understanding.

Handle Ambiguity

If the question lacks detail, clearly state your assumptions before providing the answer.

Offer alternatives if multiple interpretations are possible, using the database structure as context.

Accuracy and Completeness

Ensure that all answers are technically correct according to the provided database schema.

Avoid adding extra information or assumptions beyond the schema unless explicitly stated.

{question}
""")

        # Build the chain
        qa_chain = prompt | llm | StrOutputParser()

        # Call the LLM
        with st.spinner("Generating answer..."):
            try:
                answer = qa_chain.invoke({"question": question})
                st.success("Answer generated!")
                st.markdown("### 🧠 Answer")
                st.write(answer)
            except Exception as e:
                st.error(f"❌ Error: {e}")
