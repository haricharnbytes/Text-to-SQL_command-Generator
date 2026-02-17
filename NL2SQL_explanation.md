# 📘 Code Explanation – Natural Language 2 SQL

This document explains the implementation of the NL2SQL AI Assistant built using LangChain and Groq.

---

## Import Dependencies

```python
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
```

- os - used to access environement variables.

- load_dotenv - loads environment variables from a .env file.

- ChatGroq - LangChain wrapper for Groq-hosted LLM models.

- ChatPromptTemplate - Used to create structured prompts for the language model.

- StrOutputParser - Converts the LLM output into a clean string format.


## Load Environment Variables

```
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

```

- Loads the .env file.
- Retrieves the GROQ_API_KEY securely.
- if API key is not found, raises error.

## LLM

```
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3
)
```
- model you can choose any model you want to use.


## Prompt Template

```
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
```

The prompt:

- Defines the assistant’s role (Database Expert)

- Forces schema analysis before answering

- Prevents hallucinated columns/tables

- Requires explicit table and column references

- Ensures structured responses

- Handles ambiguity carefully

{question} placeholder inserts the user’s input

## LangChain Pipeline

```
qa_chain = prompt | llm | StrOutputParser()

```

- prompt → formats input

- llm → generates response

- StrOutputParser() → converts output to plain string

## User Input and Chain

```
question = input("💬 Ask your question: ")

try:
    answer = qa_chain.invoke({"question": question})
    print("\n🧠 Answer:\n")
    print(answer)

except Exception as e:
    print(f"\n❌ Error: {e}")
```

- Takes database-related question from user.
- runs the Chain and gie answers.