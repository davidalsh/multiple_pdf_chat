from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS


class ConversationChain:
    def __init__(self, vectorstore: FAISS):
        self.vectorstore = vectorstore
        self.llm = ChatOpenAI()
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    def get_conversation_chain(self) -> ConversationalRetrievalChain:
        return ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(),
            memory=self.memory,
        )
