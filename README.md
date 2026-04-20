# 🤖 Multi-Agent Research System

A Streamlit-based AI application that uses multiple agents to research a topic, summarize findings, generate a polished article, and critique the output.

## 🚀 Features

* 🔎 Search Agent for gathering information
* 📘 Reader Agent for summarization
* ✍️ Writer Agent for article generation
* 🧠 Critic Agent for feedback and improvements
* 💬 Beautiful ChatGPT-style Streamlit UI
* 🔐 Environment variable support with `.env`
* ⚡ Fast Python package management with `uv`

## 📁 Project Structure

```text
Multi-agent-research-system/
├── app.py
├── pipeline.py
├── agents.py
├── tools.py
├── requirements.txt
├── .env
└── README.md
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
