# Order Support Agent

Proyecto de búsqueda semántica para políticas de soporte de pedidos.

## Estado actual

- Entorno creado con Python 3.12.
- Sentence Transformers funcionando.
- Modelo `all-MiniLM-L6-v2` carga correctamente.
- Embeddings generados correctamente.
- ChromaDB crea la base local.
- Pendiente: resolver crash de ChromaDB al guardar documentos en Windows.

## Error actual

Al ejecutar:

```bash
python .\src\ingest.py