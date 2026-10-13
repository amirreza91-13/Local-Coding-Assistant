import streamlit as st
from pathlib import Path

from core.chat import ask
from utils.chat_storage import save_chat, load_chat
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
CSS_FILE = BASE_DIR / "assets" / "css" / "style.css"
LOGO_FILE = BASE_DIR / "assets" / "logo.png"

# =====================================
# LOAD CSS
# =====================================

if CSS_FILE.exists():
    with CSS_FILE.open(encoding="utf-8") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================
# SESSION
# =====================================

if "messages" not in st.session_state:
    try:
        st.session_state.messages = load_chat()
        st.session_state.history_load_error = None
    except RuntimeError as exc:
        st.session_state.messages = []
        st.session_state.history_load_error = str(exc)

if st.session_state.get("history_load_error"):
    st.warning(
        "Saved chat history could not be loaded. A recovery copy may have "
        "been created; check the details below before continuing."
    )
    st.caption(st.session_state.history_load_error)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:
    if LOGO_FILE.exists():
        st.image(str(LOGO_FILE), width=160)

    st.markdown("## MIRHAJ AI")
    st.caption("Local AI Workspace")
    st.divider()

    model = st.selectbox(
        "🧠 Model",
        [
            "qwen2.5-coder:3b",
            "qwen3:0.6b",
        ],
    )

    memory = st.slider("💾 Recent messages to include", 1, 10, 5)

    st.divider()
    st.markdown(
        f"### Current Model\n\n**{model}**\n\n"
        f"History window: **{memory} messages**"
    )

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.history_load_error = None
        save_chat(st.session_state.messages)
        st.rerun()

    st.divider()
    st.markdown("### Powered By")
    st.markdown("🟣 Streamlit\n\n🦙 Ollama")

# =====================================
# HERO
# =====================================

st.markdown(
    """
<div class="hero">
  <h1>MIRHAJ AI STUDIO</h1>
  <p>Local inference • Model choice • Chat history</p>
</div>
""",
    unsafe_allow_html=True,
)

# =====================================
# CHAT HISTORY
# =====================================

if not st.session_state.messages:
    st.info(
        """
### Welcome

Try asking:
- سلام، خودت را معرفی کن
- Build a Login Page in React
- Explain Python Decorators
- Write a SQL Query
"""
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =====================================
# CHAT INPUT AND RESPONSE
# =====================================

prompt = st.chat_input("Ask anything...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    save_chat(st.session_state.messages)
    st.session_state.history_load_error = None

    with st.chat_message("user"):
        st.markdown(prompt)

    # Use prior messages as context; core.chat adds the system prompt itself.
    history = st.session_state.messages[:-1][-memory:]

    with st.chat_message("assistant"):
        with st.spinner("Mirhaj AI is thinking..."):
            try:
                with Timer() as timer:
                    response = ask(
                        model_name=model,
                        history=history,
                        user_message=prompt,
                    )
            except Exception as exc:
                st.error(
                    "Could not get a response from Ollama. Check that Ollama "
                    "is running and the selected model is installed."
                )
                st.caption(f"Technical detail: {exc}")
            else:
                st.markdown(response)
                st.caption(f"Response time: {timer.elapsed} sec")
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                save_chat(st.session_state.messages)
