An agent-orchestrated enterprise intelligence layer that performs context-aware retrieval, enforces grounding via citations, and streams answers in real time.

python -m venv venv
venv\Scripts\Activate.ps1

System Flow

User query → Streamlit UI

Flask SocketIO backend receives query

Query Planner Agent selects retrieval strategy

Hybrid Retriever fetches enterprise knowledge

Answer Synthesizer generates grounded response

Citations + answer streamed back to UI