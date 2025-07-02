# 🛒 Ecommerce Chatbot using LLaMA 3, LangChain, and Flask
⚡ Offline AI chatbot for ecommerce — built with LangChain, LLaMA 3 (Ollama), and Flask. Supports smart Q&amp;A and RAG-style contextual answers.

This is a fully **local, offline chatbot** built using:

- **🧠 LLaMA 3 (via Ollama)**  
- **🔗 LangChain for prompt templates**  
- **🌐 Flask for web interface**

It supports:
- ✅ General Q&A (like "What is Python?")
- ✅ Context-based Q&A (like "What is your return policy?")

> ⚡ Ideal for ecommerce stores that want an AI assistant without using cloud APIs.

---

## 📌 Features

- Works 100% locally with open-source LLaMA 3 (no OpenAI API needed)
- Contextual answers from business-specific data
- Web-based Chat UI using Flask & HTML
- Built-in support for two chains:
  - `question`: general Q&A
  - `context + question`: smart, context-aware answering
- Extendable for any ecommerce or knowledge base domain

---

## 🏗️ Project Structure
ecommerce-ai-chatbot-llama3/
│
├── app.py # Flask app with UI + backend routes
├── context_data.py # Holds context data and chain logic
├── requirements.txt # All dependencies
│
├── templates/
│ └── chat.html # Web UI for chat
│
├── static/
│ └── style.css # Basic styling
│
├── pycache/ # Auto-generated Python cache

---

## 🛠️ Setup Instructions (Step-by-Step)

```bash
1. Clone the Repo

git clone https://github.com/YOUR_USERNAME/ecommerce_chatbot.git
cd ecommerce_chatbot

2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate      # For Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

🤖 Setup LLaMA 3 with Ollama

4. Install Ollama

➡️ Download from: https://ollama.com/download
Install as per your OS (Windows, Mac, Linux)

5. Start Ollama Server

ollama serve
ollama run llama3

6. Run LLaMA 3 Model

ollama run llama3

7. 🚀 Run the Chatbot (Web App)

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
