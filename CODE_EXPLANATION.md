# 📘 Code Explanation – Database-Aware AI Assistant

This document explains the implementation of the Database-Aware AI Assistant built using LangChain and Groq.

---

## Import Dependencies

```python
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
```

os - used to access environement variables.

load_dotenv - loads environment variables from a .env file.

ChatGroq - LangChain wrapper for Groq-hosted LLM models.

ChatPromptTemplate - Used to create structured prompts for the language model.

StrOutputParser - Converts the LLM output into a clean string format.


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



