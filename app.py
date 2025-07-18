from fastapi import FastAPI
from dotenv import dotenv_values
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# Load environment variables
env = dotenv_values(".env")

# Initialize OpenAI client
client = OpenAI(api_key=env["OPENAI_API_KEY"])

@app.get("/")
def home():
    return {
        "message": "Real Estate Chatbot API is running!",
        "openai_key_loaded": bool(env.get("OPENAI_API_KEY"))
    }

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_with_bot(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.message}]
        )
        reply = response.choices[0].message.content
        return {"reply": reply}
    except Exception as e:
        return {"error": str(e)}


