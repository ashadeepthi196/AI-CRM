from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",   # ✅ latest working model
    groq_api_key=groq_api_key
)

def agent_flow(input_text: str):
    try:
        response = llm.invoke(input_text)
        return {"response": response.content}
    except Exception as e:
        return {"error": str(e)}