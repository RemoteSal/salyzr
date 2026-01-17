# Enterprise Intelligence Search (Agentic RAG)

## Overview
Enterprise Intelligence Search is an agent-orchestrated Retrieval-Augmented Generation (RAG) system designed for high-fidelity enterprise knowledge discovery.  
It moves beyond basic semantic search by combining query planning, hybrid retrieval, grounded answer synthesis, and real-time streaming delivery.

The system is optimized for accuracy, explainability, and extensibility in enterprise environments.


## Core Capabilities
- Context-aware query planning via agents
- Hybrid retrieval (semantic + keyword / structured)
- Grounded answer synthesis with citation enforcement
- Real-time token streaming using WebSockets
- Modular, extensible agent architecture
- Enterprise-ready separation of ingestion, retrieval, and generation

---

## High-Level Architecture

**User Query**  
→ Streamlit UI  
→ Flask + Socket.IO Backend  
→ Query Planner Agent  
→ Hybrid Retriever  
→ Answer Synthesizer  
→ Grounded Answer + Citations  
→ Streamed back to UI in real time

---

## Tech Stack
- **Backend:** Python, Flask, Socket.IO
- **Frontend:** Streamlit
- **LLM Runtime:** Ollama (local inference)
- **Retrieval:** Vector + traditional retrieval (hybrid)
- **Architecture Pattern:** Agent-orchestrated RAG

---

## Setup Instructions

### 1. Create and Activate Virtual Environment
```bash
python -m venv venv
```

Windows
```
venv\Scripts\Activate.ps1
```

macOS / Linux
```
source venv/bin/activate
```

### 2.Install Dependencies
pip install -r requirements.txt

### 3. Run Ingestion Pipeline
```
python -m backend.ingestion.ingest
```

This step processes enterprise data and prepares it for hybrid retrieval.

### 4. Start the Application

- Start backend (Flask + Socket.IO)
- Launch Streamlit UI
- Submit queries and receive grounded, streamed responses

### Design Principles

- Grounded Answers First: Every response is citation-backed
- Agentic Control: Retrieval strategies are dynamically selected
- Streaming UX: Answers stream progressively for responsiveness
- Local-First AI: Supports offline and privacy-sensitive environments

### Architecutre diagram (Mermaid flowchart LR)

    U[User] -->|Query| UI[Streamlit UI]

    UI -->|WebSocket| BE[Flask + Socket.IO Backend]

    BE --> QP[Query Planner Agent]

    QP -->|Strategy Selection| HR[Hybrid Retriever]
    HR -->|Semantic Search| VS[Vector Store]
    HR -->|Keyword / Structured| KS[Enterprise Data Sources]

    VS --> HR
    KS --> HR

    HR --> AS[Answer Synthesizer Agent]

    AS -->|Grounded Answer + Citations| BE
    BE -->|Token Stream| UI
    UI -->|Rendered Response| U


#### License

This project is released under the MIT License unless stated otherwise.
Third-Party Acknowledgements

This project uses Ollama for local LLM inference.
Ollama is distributed under its own license terms.
See: https://github.com/ollama/ollama
