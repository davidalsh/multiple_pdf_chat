import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from app.conversation_chain import ConversationChain
from app.pdf_handler import PDFHandler
from app.streamlit_page import StreamlitPdfChatPage


class PdfChatApp:
    def __init__(self, title: str, icon: str):
        load_dotenv()
        self.page = StreamlitPdfChatPage(title, icon)
        self.pdf_handler_class = PDFHandler

    def render_ui(self):
        self.page.setup_config()
        st.header(f"{self.page.title} {self.page.icon}")
        user_question = st.text_input("Ask a question about your documents:")
        if user_question:
            self.page.update_chat_history(user_question)

        with st.sidebar:
            st.subheader("Your documents")
            pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
            pdf_handler = self.pdf_handler_class(pdf_docs)
            if st.button("Process"):
                with st.spinner("Processing"):
                    text_chunks = pdf_handler.get_text_chunks()
                    vectorstore = self.get_vectorstore(text_chunks)
                    st.session_state.conversation = ConversationChain(vectorstore).get_conversation_chain()

    @staticmethod
    def get_vectorstore(text_chunks: list) -> FAISS:
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
        return vectorstore

    def run(self):
        self.render_ui()
