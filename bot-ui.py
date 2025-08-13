import os
import streamlit as st
from dotenv import load_dotenv
from llm_bot import get_openai_response

load_dotenv()

st.title("UtilityBot - your utility network AI assistant........")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hi, I am UtilityBot representative - how can I help you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = get_openai_response(prompt, [(m["role"], m["content"]) for m in st.session_state.messages])
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    