from pathlib import Path
import traceback

import chromadb
from sentence_transformers import SentenceTransformer


try:
    print("1 - Inicio ingest", flush=True)

    BASE_DIR = Path(__file__).resolve().parents[1]
    DATA_FILE = BASE_DIR / "data" / "policies.txt"
    CHROMA_PATH = str(BASE_DIR / "chroma_db")

    print("2 - Archivo:", DATA_FILE, flush=True)

    texts = [
        line.strip()
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    print("3 - Textos encontrados:", len(texts), flush=True)

    print("4 - Cargando modelo...", flush=True)
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("5 - Generando embeddings...", flush=True)
    embeddings = model.encode(texts).tolist()

    print("6 - Conectando a ChromaDB...", flush=True)
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(name="order_policies")

    ids = [f"doc_{i}" for i in range(len(texts))]

    print("7 - Guardando documentos...", flush=True)
    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
    )

    print("8 - Documentos cargados:", len(texts), flush=True)
    print("9 - Total en ChromaDB:", collection.count(), flush=True)

except Exception:
    print("ERROR:", flush=True)
    traceback.print_exc()