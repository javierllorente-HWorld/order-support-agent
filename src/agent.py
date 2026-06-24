from pathlib import Path
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parents[1]
INDEX_PATH = str(BASE_DIR / "faiss_index" / "index.faiss")
TEXTS_PATH = str(BASE_DIR / "faiss_index" / "texts.json")

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(INDEX_PATH)
with open(TEXTS_PATH, encoding="utf-8") as f:
    texts = json.load(f)

def buscar(query, k=2):
    embedding = model.encode([query]).astype("float32")
    distancias, indices = index.search(embedding, k)
    resultados = [texts[i] for i in indices[0] if i < len(texts)]
    return resultados

def agente(pregunta):
    print("\nPregunta:", pregunta)
    resultados = buscar(pregunta)
    print("Politicas relevantes encontradas:")
    for r in resultados:
        print(" -", r)
    print("Recomendacion: Revisar las politicas anteriores para responder al cliente.")

if __name__ == "__main__":
    agente("El cliente quiere devolver un producto")
    agente("Cuanto cuesta el envio?")
