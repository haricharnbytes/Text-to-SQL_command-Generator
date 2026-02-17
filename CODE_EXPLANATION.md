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
