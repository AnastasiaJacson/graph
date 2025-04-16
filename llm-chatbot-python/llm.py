from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings


llm = ChatOllama(model="gemma3:4b")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
