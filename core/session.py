import streamlit as st


def initialize():

    if "messages" not in st.session_state:

        st.session_state.messages = []

    if "memory" not in st.session_state:

        st.session_state.memory = 5

    if "model" not in st.session_state:

        st.session_state.model = "qwen2.5-coder:3b"