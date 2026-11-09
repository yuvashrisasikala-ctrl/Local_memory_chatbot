
import os
import json
import uuid
import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="NEXIRAB AI",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------- CSS DESIGN ----------------

st.markdown("""
<style>

html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background-color: #101D2E !important;
    color: #F8FAFC !important;
}

header[data-testid="stHeader"] {
    background: #101D2E !important;
}

section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div {
    background-color: #152438 !important;
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] span {
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] [data-baseweb="select"],
section[data-testid="stSidebar"] [role="combobox"] {
    background-color: #20364A !important;
    color: #FFFFFF !important;
    border-color: #5EEAD4 !important;
}

[data-baseweb="popover"],
[data-baseweb="menu"],
[role="listbox"],
[role="option"] {
    background-color: #20364A !important;
    color: #FFFFFF !important;
}

.stTextInput input,
.stTextArea textarea {
    background-color: #20364A !important;
    color: #FFFFFF !important;
}

.stButton button {
    background-color: #0D9488 !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
}

.stButton button:hover {
    background-color: #14B8A6 !important;
}

[data-testid="stChatMessage"] {
    background-color: #1B3045 !important;
    border-radius: 12px !important;
}

.nexirab-title {
    text-align: center;
    color: #5EEAD4;
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 5px;
}

.nexirab-subtitle {
    text-align: center;
    color: #CBD5E1;
    font-size: 17px;
    margin-bottom: 30px;
}

footer {
    visibility: hidden;
}

/* CHAT MESSAGE TEXT - WHITE COLOR */

[data-testid="stChatMessage"],
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] span,
[data-testid="stChatMessage"] div,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] strong {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

/* CHAT INPUT TEXT */

[data-testid="stChatInput"] textarea {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

</style>
""", unsafe_allow_html=True)


# ---------------- CHAT STORAGE ----------------

CHAT_FILE = "nexirab_chats.json"


def load_chats():
    if os.path.exists(CHAT_FILE):
        try:
            with open(CHAT_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_chats():
    with open(CHAT_FILE, "w", encoding="utf-8") as file:
        json.dump(
            st.session_state.chats,
            file,
            indent=4,
            ensure_ascii=False
        )


# ---------------- SESSION INITIALIZATION ----------------

if "chats" not in st.session_state:
    st.session_state.chats = load_chats()

if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

if "model" not in st.session_state:
    st.session_state.model = "qwen2.5:3b"

if "memory_type" not in st.session_state:
    st.session_state.memory_type = "Full Conversation"


def create_new_chat():
    chat_id = str(uuid.uuid4())

    st.session_state.chats[chat_id] = {
        "title": "New Chat",
        "messages": []
    }

    st.session_state.current_chat = chat_id
    save_chats()


if (
    st.session_state.current_chat is None
    or st.session_state.current_chat not in st.session_state.chats
):
    create_new_chat()


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("## 💬 NEXIRAB AI")

    st.markdown("---")

    if st.button("➕ New Chat", use_container_width=True):
        create_new_chat()
        st.rerun()

    st.markdown("### ⚙️ Settings")

    model_options = [
        "qwen2.5:3b",
        "gemma3:1b",
        "llama3.2",
        "mistral"
    ]

    selected_model = st.selectbox(
        "Select AI Model",
        model_options,
        index=model_options.index(st.session_state.model)
        if st.session_state.model in model_options else 0
    )

    st.session_state.model = selected_model

    memory_options = [
        "Full Conversation",
        "Last 5 Messages",
        "Last 10 Messages"
    ]

    selected_memory = st.selectbox(
        "Conversation Memory",
        memory_options,
        index=memory_options.index(st.session_state.memory_type)
    )

    st.session_state.memory_type = selected_memory

    st.markdown("---")

    st.markdown("### 📚 Chat History")

    chat_ids = list(st.session_state.chats.keys())

    for chat_id in reversed(chat_ids):

        chat_title = st.session_state.chats[chat_id]["title"]

        if st.button(
            f"💬 {chat_title}",
            key=f"chat_{chat_id}",
            use_container_width=True
        ):
            st.session_state.current_chat = chat_id
            st.rerun()

    st.markdown("---")

    if st.button("🗑️ Clear Current Chat", use_container_width=True):

        current_id = st.session_state.current_chat

        st.session_state.chats[current_id]["messages"] = []
        st.session_state.chats[current_id]["title"] = "New Chat"

        save_chats()
        st.rerun()


# ---------------- MAIN TITLE ----------------

st.markdown(
    '<div class="nexirab-title">💬 NEXIRAB AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="nexirab-subtitle">'
    'Your Intelligent AI Chat Assistant'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- CURRENT CHAT ----------------

current_id = st.session_state.current_chat
current_chat = st.session_state.chats[current_id]
messages = current_chat["messages"]


# ---------------- DISPLAY CHAT HISTORY ----------------

for message in messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------- AI RESPONSE FUNCTION ----------------

def get_ai_response(user_input, chat_messages):

    model = ChatOllama(
        model=st.session_state.model,
        temperature=0.7
    )

    if st.session_state.memory_type == "Last 5 Messages":
        history = chat_messages[-5:]

    elif st.session_state.memory_type == "Last 10 Messages":
        history = chat_messages[-10:]

    else:
        history = chat_messages

    context = ""

    for message in history:
        role = message["role"].upper()
        content = message["content"]
        context += f"{role}: {content}\n"

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are NEXIRAB AI, a helpful and friendly AI assistant. "
            "Answer clearly and accurately."
        ),
        (
            "human",
            "Previous conversation:\n{context}\n\n"
            "User question: {question}"
        )
    ])

    formatted_messages = prompt.format_messages(
        context=context,
        question=user_input
    )

    response = model.invoke(formatted_messages)

    return response.content


# ---------------- CHAT INPUT ----------------

user_input = st.chat_input("Message NEXIRAB AI...")

if user_input:

    messages.append({
        "role": "user",
        "content": user_input
    })

    if current_chat["title"] == "New Chat":
        current_chat["title"] = user_input[:30]

    save_chats()

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("NEXIRAB AI is thinking..."):

            try:
                answer = get_ai_response(
                    user_input,
                    messages[:-1]
                )

                st.markdown(answer)

                messages.append({
                    "role": "assistant",
                    "content": answer
                })

                save_chats()

            except Exception as error:

                error_message = (
                    "Unable to connect to Ollama. "
                    "Please check whether Ollama is running "
                    "and the selected model is installed.\n\n"
                    f"Error: {error}"
                )

                st.error(error_message)


# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    "<center style='color:#94A3B8;'>"
    "Powered by NEXIRAB AI | Built with Streamlit and Ollama"
    "</center>",
    unsafe_allow_html=True
)
