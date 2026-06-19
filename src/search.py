from pathlib import Path
import sys

import chromadb
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parents[1]
CHROMA_PATH = str(BASE_DIR / "chroma_db")

question = " ".join(sys.argv[1:])

if not question:
    question = input("Pregunta: ")

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection(name="order_policies")

question_embedding = model.encode([question])[0].tolist()

results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3,
)

print("\nPregunta:")
print(question)

print("\nDocumentos encontrados:")
for document, distance in zip(results["documents"][0], results["distances"][0]):
    print(f"- {document} | distancia: {distance:.4f}")