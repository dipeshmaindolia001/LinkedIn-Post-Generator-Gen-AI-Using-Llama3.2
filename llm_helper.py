from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
import streamlit as st

load_dotenv()  # works locally via .env

# fall back to Streamlit secrets when deployed
api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.3-70b-versatile"
)

if __name__ == "__main__":
    response = llm.invoke("who is dipesh maindolia")
    print(response.content)