from pathlib import Path
import traceback
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

try:
    print("1 - Inicio ingest")

    BASE_DIR = Path(__file__).resolve().parents[1]
    DATA_FILE = BASE_DIR / "data" / "policies.txt"
    INDEX_PATH = str(BASE_DIR / "faiss_index" / "index.faiss")
    TEXTS_PATH = str(BASE_DIR / "faiss_index" / "texts.json")

    Path(INDEX_PATH).parent.mkdir(exist_ok=True)

    print("2 - Archivo:", DATA_FILE)

    texts = [
        line.strip()
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    print("3 - Textos encontrados:", len(texts))
    print("4 - Cargando modelo...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("5 - Generando embeddings...")
    embeddings = model.encode(texts)
    embeddings = np.array(embeddings).astype("float32")

    print("6 - Creando indice FAISS...")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    print("7 - Guardando en disco...")
    faiss.write_index(index, INDEX_PATH)
    with open(TEXTS_PATH, "w", encoding="utf-8") as f:
        json.dump(texts, f, ensure_ascii=False)

    print("8 - Documentos guardados:", len(texts))
    print("9 - Total en indice:", index.ntotal)

except Exception:
    print("ERROR:")
    traceback.print_exc()
