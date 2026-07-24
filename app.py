import logging
import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from chatbot import get_response

st.title("English Tutor Chatbot")
st.caption("A friendly English Tutor!")

if not os.getenv("OPENAI_API_KEY"):
    st.error("OPENAI_API_KEY is not set. Add it to the .env file in this folder.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages=[]

if st.button("Clear chat:"):
    st.session_state.messages=[]
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])

if prompt := st.chat_input("Type your message"):
    with st.chat_message("user"):
        st.write(prompt)
    outgoing = st.session_state.messages + [{"role":"user","content":prompt}]
    with st.chat_message("assistant"):
        try:
            reply = get_response(outgoing)
            st.write(reply)
            st.session_state.messages.append({'role':'user',"content":prompt})
            st.session_state.messages.append({'role':'assistant',"content":reply})
        except Exception:
            logging.exception("get_response failed")
            st.error("Sorry, something went wrong. Please try again later.")

