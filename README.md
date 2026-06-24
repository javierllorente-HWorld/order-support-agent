# Order Support Agent

Agente que ayuda al equipo de soporte a encontrar rapidamente que politica aplica segun la consulta de un cliente.

## Que hace

Le escribis una pregunta (por ejemplo: el cliente quiere devolver un producto) y el agente busca automaticamente en las politicas del negocio cuales son las mas relevantes para responder.

## Estado actual

* Funciona de punta a punta.
* Lee las politicas desde un archivo de texto.
* Encuentra las politicas mas relevantes por significado, no por palabras exactas.
* Guarda el indice localmente para no reprocesar todo cada vez.

## Como usarlo

Primero, cargar las politicas (solo la primera vez o cuando cambien):

python src/ingest.py

Despues, consultar el agente:

python src/agent.py
"@ | Set-Content README.md -Encoding UTF8
