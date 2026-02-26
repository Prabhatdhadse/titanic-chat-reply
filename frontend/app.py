import streamlit as st
import requests
import os

for img in ["age_hist.png", "fare_hist.png", "survival_chart.png"]:
    path = f"../backend/{img}"
    if os.path.exists(path):
        st.image(path)

st.set_page_config(page_title="Titanic AI Chat", page_icon="🚢", layout="wide")

st.title("🚢 Titanic Dataset Chat Agent")
st.caption("Ask anything about Titanic passengers")

if "chat" not in st.session_state:
    st.session_state.chat = []

question = st.chat_input("Ask question...")

if question:
    st.session_state.chat.append(("user", question))

    res = requests.get(
        "https://titanic-chat-reply.onrender.com/",
        params={"q": question}
    ).json()["answer"]

    st.session_state.chat.append(("bot", res))

for role, msg in st.session_state.chat:
    if role == "user":
        with st.chat_message("user"):
            st.write(msg)
    else:
        with st.chat_message("assistant"):
            st.write(msg)