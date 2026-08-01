import streamlit as st
from pathlib import Path

from core.chat import ask
from utils.chat_storage import save_chat, load_chat
from utils.exporter import export_txt, export_json
from utils.timer import Timer

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Mirhaj AI Studio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# PATHS
# =====================================

BASE_DIR = Path(__file__).parent

CSS_FILE = BASE_DIR / "css" / "style.css"
LOGO_FILE = BASE_DIR / "assets" / "logo.svg"

# =====================================
# LOAD CSS
# =====================================

if CSS_FILE.exists():
    with open(CSS_FILE, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================
# SESSION
# =====================================

if "messages" not in st.session_state:

    st.session_state.messages = load_chat()
# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    if LOGO_FILE.exists():
        st.image(str(LOGO_FILE), width=160)

    st.markdown("## MIRHAJ AI")

    st.caption("Offline AI Workspace")

    st.divider()

    model = st.selectbox(
        "🧠 Model",
        [
            "qwen2.5-coder:3b",
            "qwen3:0.6b"
        ]
    )

    memory = st.slider(
        "💾 Memory",
        1,
        10,
        5
    )

    st.divider()

    st.success(
        f"""
### Current Model

**{model}**

Memory : **{memory}**
"""
    )

    if st.button(
        "🗑 Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("### Powered By")

    st.markdown("""
🟣 Streamlit

➕

🦙 Ollama
""")

# =====================================
# HERO
# =====================================

st.markdown(
    """
<div class="hero">

<h1>MIRHAJ AI STUDIO</h1>

<p>
Offline • Private • Fast
</p>

</div>
""",
    unsafe_allow_html=True
)

# =====================================
# WELCOME SCREEN
# =====================================

if len(st.session_state.messages) == 0:

    st.info(
        """
### 👋 Welcome

Try asking:

- سلام، خودت را معرفی کن
- Build a Login Page in React
- Explain Python Decorators
- Write a SQL Query
"""
    )

# =====================================
# SHOW CHAT
# =====================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =====================================
# INPUT
# =====================================

prompt = st.chat_input("Ask anything...")

# =====================================
# CHAT
# =====================================

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )
    save_chat(st.session_state.messages)

    with st.chat_message("user"):
        st.markdown(prompt)

    history = st.session_state.messages[-memory:]

with st.chat_message("assistant"):

    with st.spinner("Mirhaj AI is thinking..."):

        with Timer() as t:
            history = []

            response = ask(
                model_name=model,
                history=history,
                user_message=prompt
            )

        st.markdown(response)
        st.caption(f"⚡ Response Time : {t.elapsed} sec")
        st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    save_chat(st.session_state.messages)