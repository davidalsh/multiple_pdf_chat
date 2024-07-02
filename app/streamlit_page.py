import streamlit as st
from html_templates import user_template, bot_template, css


class StreamlitPage:
    def __init__(self, title: str, icon: str):
        self.title = title
        self.icon = icon
        self.css = css
        self._setup_session_state()

    def setup_config(self):
        st.set_page_config(page_title=self.title, page_icon=self.icon)
        st.write(self.css, unsafe_allow_html=True)

    @staticmethod
    def _setup_session_state():
        pass


class StreamlitPdfChatPage(StreamlitPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_template = user_template
        self.bot_template = bot_template

    @staticmethod
    def _setup_session_state():
        if "conversation" not in st.session_state:
            st.session_state.conversation = None
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = None

    def update_chat_history(self, user_question: str):
        response = st.session_state.conversation({"question": user_question})
        st.session_state.chat_history = response["chat_history"]
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(self.user_template.replace("{{ message }}", message.content), unsafe_allow_html=True)
            else:
                st.write(self.bot_template.replace("{{ message }}", message.content), unsafe_allow_html=True)
