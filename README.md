# 🤖 Multi-Agent Research System

[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/sudhir1992/Multi-Agent-Research-System)
[![Live Demo](https://huggingface.co/spaces/sudhir1992/Multi-Agent-Research-System)

A Streamlit-based AI application that uses multiple agents to research a topic, summarize findings, generate a polished article, and critique the output.

---
## 🔗 Live Demo
Aap is project ko yahan live test kar sakte hain:  
👉 **[Hugging Face Space: Multi-Agent Research System](https://huggingface.co/spaces/sudhir1992/Multi-Agent-Research-System)**
---

## 🚀 Features

* 🔎 **Search Agent:** Internet se topic ke baare mein latest information gather karta hai.
* 📘 **Reader Agent:** Lambe articles aur sources ko summarize karke core details nikalta hai.
* ✍️ **Writer Agent:** Gathered research ko ek professional aur well-structured report mein convert karta hai.
* 🧠 **Critic Agent:** Final report ko evaluate karke feedback aur score (X/10) deta hai.
* 💬 **Beautiful UI:** ChatGPT-style Streamlit interface for easy interaction.
* 🔐 **Environment Support:** Secure API key management using `.env`.
* ⚡ **Optimized Performance:** Fast package management with `uv`.

## 📁 Project Structure

```text
Multi-agent-research-system/
├── app.py           # Streamlit Frontend
├── pipeline.py      # Core logic connecting agents
├── agents.py        # Agent definitions and prompts
├── tools.py         # Search and Scraping functions
├── requirements.txt # Project dependencies
├── Dockerfile       # Deployment configuration
└── README.md        # Documentation
```

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Multi-agent-research-system
```

### 2. Create Virtual Environment

```bash
uv venv
```

### 3. Activate Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
uv pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the root folder:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## ▶️ Run the Application

```bash
uv run streamlit run app.py
```

Then open: `http://localhost:8501`

## 🧪 Example Usage

Enter a topic like:

* Artificial Intelligence Trends 2026
* Future of DevOps with AI
* Generative AI in Healthcare

## 📦 requirements.txt Example

```txt
streamlit
langchain
langchain-openai
langchain-community
python-dotenv
tavily-python
```

## 🚀 Future Enhancements

* File upload + RAG
* PDF export
* Voice input
* Chat history database
* Deploy to AWS / Render / Docker

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

## 📄 License

MIT License
