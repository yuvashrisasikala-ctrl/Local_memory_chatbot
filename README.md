# 💬 NEXIRAB AI – Intelligent AI Chat Assistant

## 📌 Project Overview

NEXIRAB AI is an intelligent AI-powered chatbot application developed using Python, Streamlit, LangChain, and Ollama.

It provides a user-friendly interface where users can interact with locally running AI language models and receive intelligent responses.

## ✨ Features

- 💬 Interactive AI Chat Interface
- 🤖 Multiple AI Model Support
- 🧠 Conversation Memory Management
- 📚 Chat History Storage
- ➕ Create New Chat
- 🗑️ Clear Current Chat
- 💾 Automatic Chat Saving using JSON
- 🎨 Modern Dark Theme UI
- ⚡ Local AI Responses using Ollama

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Ollama
- JSON

## 🤖 Supported AI Models

- Qwen 2.5 (3B)
- Gemma 3 (1B)
- Llama 3.2
- Mistral

## 📂 Project Structure

    NEXIRAB-AI/
    │
    ├── app.py
    ├── nexirab_chats.json
    ├── README.md
    └── requirements.txt

## ⚙️ Installation and Setup

### 1. Install Python

Download Python from:

https://www.python.org/downloads/

### 2. Install Ollama

Download Ollama from:

https://ollama.com/

### 3. Clone the Repository

    git clone YOUR_GITHUB_REPOSITORY_URL

### 4. Open Project Folder

    cd NEXIRAB-AI

### 5. Install Required Libraries

    pip install streamlit langchain-ollama langchain-core

### 6. Download AI Model

    ollama pull qwen2.5:3b

### 7. Run the Application

    streamlit run app.py

## 🧠 Conversation Memory

NEXIRAB AI provides three conversation memory options:

1. Full Conversation – Uses the complete conversation as context.
2. Last 5 Messages – Uses the latest 5 messages as context.
3. Last 10 Messages – Uses the latest 10 messages as context.

## 💡 How It Works

1. The user enters a question in the chat interface.
2. The application collects previous conversation history.
3. LangChain formats the prompt.
4. Ollama generates an AI response.
5. The response is displayed in the Streamlit interface.
6. Chat messages are saved in a JSON file.

## 🎯 Project Objective

The main objective of NEXIRAB AI is to develop a smart and interactive AI chatbot that runs locally using Ollama.

It aims to provide intelligent responses, maintain conversation history, and support multiple language models through a simple and attractive interface.

## 🚀 Future Enhancements

- Voice Input and Output
- Image Upload Support
- PDF Question Answering
- User Authentication
- Improved Long-Term Memory
- More AI Model Integrations
