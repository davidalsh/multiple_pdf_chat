from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter


class PDFHandler:
    def __init__(self, docs: list):
        self.docs = docs
        self._reader = PdfReader
        self.raw_text = self._get_raw_text()

    def _get_raw_text(self):
        raw_text = ""
        for pdf in self.docs:
            pdf_reader = self._reader(pdf)
            for page in pdf_reader.pages:
                raw_text += page.extract_text()
        return raw_text

    def get_text_chunks(self) -> list:
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        chunks = text_splitter.split_text(self.raw_text)
        return chunks
