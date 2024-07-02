from app.chat_app import PdfChatApp

if __name__ == "__main__":
    app = PdfChatApp(
        title="Chat with multiple PDFs",
        icon=":books:",
    )
    app.run()
