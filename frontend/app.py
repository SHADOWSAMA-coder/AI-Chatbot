import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot")

st.title(" AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_name = st.text_input("Enter your name", value="User")

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.chat_message("user").write(user_input)

    response = requests.post(
        "http://localhost:8000/chat",
        json={"user_name": user_name, "message": user_input},
    )

    bot_reply = response.json()["reply"]

    st.chat_message("assistant").write(bot_reply)

    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
