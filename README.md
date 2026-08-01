<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=30&duration=3000&pause=500&color=00D4FF&center=true&vCenter=true&width=700&lines=🤖+Local+Coding+Assistant;AI+Chatbot+for+Developers;Built+with+LangChain+%2B+Streamlit;Powered+by+Qwen2.5-Coder+7B" alt="Local Coding Assistant Header" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-0.2%2B-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/Ollama-0.3%2B-000000?style=for-the-badge&logo=ollama&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=amirreza91-13&label=Visitors&color=00D4FF&style=flat-square" alt="Visitors" />
  <img src="https://img.shields.io/github/stars/amirreza91-13/Local-Coding-Assistant?style=social" alt="Stars" />
  <img src="https://img.shields.io/github/forks/amirreza91-13/Local-Coding-Assistant?style=social" alt="Forks" />
</p>

---

## 🧠 About The Project

**Local Coding Assistant** is a fully **offline**, privacy-focused AI chatbot designed to help developers with coding questions, debugging, and code generation. Built with **LangChain** for intelligent conversation management and **Streamlit** for a modern, neon-themed UI, this assistant runs entirely on your local machine using **Ollama** and the powerful **Qwen2.5-Coder 7B** model.

> 🔒 **No data ever leaves your system** – complete privacy guaranteed.

<p align="center">
  <img src="assets/logo.png" alt="Local Coding Assistant Logo" width="200" style="border-radius: 15px;" />
</p>

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 🔒 **100% Local & Private** | All processing happens on your machine – no external APIs, no data collection. |
| 💻 **Coding-Focused** | Optimized for programming tasks using the Qwen2.5-Coder model. |
| 🧠 **Smart Memory** | LangChain's `ConversationChain` maintains chat history for context-aware responses. |
| 🎨 **Neon UI** | Custom Streamlit interface with a glowing blue theme and smooth animations. |
| ⚡ **Lightweight** | Runs efficiently on systems with 8–16 GB RAM (CPU-only mode supported). |
| 📁 **Structured Codebase** | Clean separation of concerns – `core/`, `ui/`, `utils/`, `assets/`. |

---

## 🛠️ Built With

<div align="center">

| Python | Streamlit | LangChain | Ollama | Qwen 2.5 |
| :---: | :---: | :---: | :---: | :---: |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" /> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg" width="60" /> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/langchain/langchain-original.svg" width="60" /> | <img src="https://ollama.com/public/ollama.png" width="60" /> | <img src="https://qwenlm.ai/assets/logo.png" width="60" /> |

</div>

---

## 📁 Project Structure

```
Local-Coding-Assistant/
├── assets/
│   ├── css/
│   │   └── style.css
│   └── logo.png
├── core/
│   ├── chat.py
│   ├── confing.py
│   ├── models.py
│   ├── prompt.py
│   └── session.py
├── ui/
│   ├── chat.py
│   ├── header.py
│   └── sidebar.py
├── utils/
│   ├── chat_storage.py
│   ├── copier.py
│   ├── exporter.py
│   ├── history.py
│   ├── regerenate.py
│   ├── search.py
│   ├── timer.py
│   └── tokenizer.py
├── .gitignore
├── main.py
├── requirements.txt
└── streamlit_ollama.py
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+** installed on your system.
- **Ollama** installed and running – [Download Ollama](https://ollama.com/download).

### Installation & Running

```bash
# 1. Clone the repository
git clone https://github.com/amirreza91-13/Local-Coding-Assistant.git
cd Local-Coding-Assistant

# 2. Create and activate a virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull the Qwen2.5-Coder model (recommended version)
ollama pull qwen2.5-coder:7b-instruct-q4_K_M

# 5. Run the Streamlit app
streamlit run streamlit_ollama.py
```

The app will open at `http://localhost:8501` in your browser.

---

## 🎯 Usage

1. **Type your coding question** in the chat input box.
2. The assistant will respond with helpful code snippets, explanations, or debugging tips.
3. The conversation history is maintained for context-aware follow-up questions.

---

## 🧪 Troubleshooting

| Issue | Solution |
| :--- | :--- |
| `NameError: name 'history' is not defined` | Make sure you're using `st.session_state` to manage chat history. |
| `Error: pull model manifest: no such host` | Change your DNS to `8.8.8.8` and `1.1.1.1`, or use a VPN. |
| Out-of-Memory (OOM) errors | Use a lighter version: `ollama pull qwen2.5-coder:7b-instruct-iq2_s`. |
| `ModuleNotFoundError` | Ensure all dependencies are installed: `pip install -r requirements.txt`. |

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or new features:

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/AmazingFeature`.
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`.
4. Push to the branch: `git push origin feature/AmazingFeature`.
5. Open a Pull Request.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 🙏 Acknowledgments

- **[LangChain](https://www.langchain.com/)** – for the incredible framework.
- **[Streamlit](https://streamlit.io/)** – for making data apps fun and easy.
- **[Ollama](https://ollama.com/)** – for seamless local model execution.
- **[Qwen](https://qwenlm.ai/)** – for the powerful coding model.

---

<p align="center">
  <b>Built with ❤️ by Amirreza</b><br>
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00D4FF&height=120&section=footer" />
</p>
