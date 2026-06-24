import chromadb
from chromadb.utils import embedding_functions

client = chromadb.EphemeralClient()
ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = client.get_or_create_collection(name="test", embedding_function=ef)
print("collection ok")

texts = ["politica de devolucion: 30 dias", "envios gratis mayores a 50 dolares"]
collection.add(ids=["doc_0", "doc_1"], documents=texts)
print("add ok")
print("total:", collection.count())
