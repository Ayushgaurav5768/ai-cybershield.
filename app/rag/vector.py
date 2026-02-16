import os
from dotenv import load_dotenv

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "knowledge_base")

def build_vector_store():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(DATA_PATH, file))
            documents.extend(loader.load())

    print("Loaded documents:", len(documents))

    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = text_splitter.split_documents(documents)

    print("Chunks created:", len(docs))

    embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


    vector_store = FAISS.from_documents(docs, embeddings)

    vector_store.save_local(os.path.join(BASE_DIR, "faiss_index"))

    print("Vector store built successfully.")

if __name__ == "__main__":
    build_vector_store()
