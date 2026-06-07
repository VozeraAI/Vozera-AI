import os

import streamlit as st

from vozerai import clean_message, get_reply, save_chat

st.set_page_config(page_title="Vozera AI", page_icon="💬", layout="centered")

st.markdown(
    """
    <style>
    .main { background: #f8fbff; }
    .vozera-card {
        padding: 1rem;
        border-radius: 1rem;
        background: linear-gradient(135deg, #eaf7ff, #f7efff);
        border: 1px solid #d7ebff;
        text-align: center;
        margin-bottom: 1rem;
    }
    .small-text { color: #58677c; font-size: 0.95rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.image("assets/vozera-logo.svg", width=260)
st.title("Vozera AI")
st.markdown(
    "<div class='vozera-card'>A beginner-friendly AI chatbot with commands, history, and Gemini API support.</div>",
    unsafe_allow_html=True,
)

api_key = os.getenv("GEMINI_API_KEY")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "gemini_history" not in st.session_state:
    st.session_state.gemini_history = []

with st.sidebar:
    st.header("Commands")
    st.write("Type one of these in the chat:")
    st.code("help\ntime\ndate\nhistory\nbye")
    st.header("Chat history")
    if len(st.session_state.chat_history) == 0:
        st.write("No chat history yet.")
    else:
        st.text("\n".join(st.session_state.chat_history))
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.session_state.chat_history = []
        st.session_state.gemini_history = []
        st.rerun()

for chat in st.session_state.messages:
    with st.chat_message(chat["role"]):
        st.write(chat["text"])

message = st.chat_input("Ask Vozera AI something...")

if message:
    st.session_state.messages.append({"role": "user", "text": message})
    with st.chat_message("user"):
        st.write(message)

    reply, should_save = get_reply(
        message,
        st.session_state.chat_history,
        st.session_state.gemini_history,
        api_key,
    )

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "text": reply})

    if should_save:
        save_chat(
            message,
            reply,
            st.session_state.chat_history,
            st.session_state.gemini_history,
        )

    if clean_message(message) == "bye":
        st.info("You can close the browser tab when you are done.")
