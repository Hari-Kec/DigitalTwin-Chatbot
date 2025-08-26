import streamlit as st
from ui_components import show_avatar, chat_interface
from chat_session import ChatSession
from config import PERSONAS

st.set_page_config(page_title="Digital Clone", page_icon="🤖", layout="centered")
st.title("🚀 Digital Clone - Persona AI Chatbot")

if "persona_choice" not in st.session_state:
    st.session_state.persona_choice = None

if "chat_session" not in st.session_state:
    st.session_state.chat_session = None

if st.session_state.persona_choice is None:
    choice = st.radio("Choose a persona:", ["Elon Musk", "Donald Trump","Amitabh Bachan","MS Dhoni","Vijay"])
    if st.button("Start Chat"):
        if choice == "Elon Musk":
            st.session_state.persona_choice = "elon_musk"
        elif choice == "Amitabh Bachan":
            st.session_state.persona_choice = "amitabh_bachchan"
        elif choice == "MS Dhoni":
            st.session_state.persona_choice = "ms_dhoni"
        elif choice == "Vijay":
            st.session_state.persona_choice = "vijay"
        else:
            st.session_state.persona_choice = "donald_trump"
        st.session_state.chat_session = ChatSession(PERSONAS[st.session_state.persona_choice])
        st.rerun()
else:
    persona = PERSONAS[st.session_state.persona_choice]
    show_avatar(persona["avatar"], persona["name"], key=f"{persona['name']}_avatar")
    chat_interface(st.session_state.chat_session)
