from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

llm = ChatOllama(model="gemma3:4b")

embeddings = OllamaEmbeddings(model="nomic-embed-text")
