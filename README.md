# Enterprise Intelligence Search (Agentic RAG)
Overview

This project implements an intelligent enterprise search system that goes beyond semantic matching by using agent-orchestrated retrieval, grounded answer synthesis, and real-time streaming responses.

## Key Capabilities

- Context-aware query planning
- Hybrid semantic retrieval
- Citation-backed answers
- Real-time streaming via WebSockets
- Modular agent architecture


###### An agent-orchestrated enterprise intelligence layer that performs context-aware retrieval, enforces grounding via citations, and streams answers in real time.

### Steps to run 
- Create & activate a virtual environment
``` python -m venv venv
    venv\Scripts\Activate.ps1
```

- System Flow

User query → Streamlit UI
Flask SocketIO backend receives query
Query Planner Agent selects retrieval strategy
Hybrid Retriever fetches enterprise knowledge
Answer Synthesizer generates grounded response
Citations + answer streamed back to UI