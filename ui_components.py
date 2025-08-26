import streamlit as st
import base64

def show_avatar(img_path, name, key):
    st.image(img_path, width=200)
    if st.button(f"💬 Chat with {name}", key=key):
        st.session_state.avatar_clicked = True

def autoplay_audio(file_path: str):
    import base64
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    md = f"""
        <audio autoplay controls>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <script>
            document.querySelectorAll("audio").forEach(el => el.play().catch(()=>{{}}));
        </script>
    """
    st.markdown(md, unsafe_allow_html=True)


def chat_interface(session):
    st.subheader(f"Chatting as {session.persona['name']}")
    user_input = st.chat_input("Type your message...")
    if user_input:
        response, audio_file = session.get_response(user_input)
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant"):
            st.markdown(response)
            autoplay_audio(audio_file)   # 🔥 Plays instantly
