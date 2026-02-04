import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
import google.generativeai as genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


app = FastAPI()


model = genai.GenerativeModel("models/gemini-2.5-flash-lite")


conversation = []

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()

    user_name = data.get("user_name", "User")
    user_message = data.get("message", "")

    
    if not conversation:
        conversation.append(
            f"You are a helpful AI chatbot talking to a user named {user_name}."
        )

    
    conversation.append(f"User: {user_message}")

    
    prompt = "\n".join(conversation)

    
    response = model.generate_content(prompt)

    bot_reply = response.text.strip()

    
    conversation.append(f"Bot: {bot_reply}")

   
    MAX_TURNS = 10
    if len(conversation) > (2 * MAX_TURNS + 1):
        conversation[:] = conversation[:1] + conversation[-(2 * MAX_TURNS):]

    return {
        "reply": bot_reply
    }
