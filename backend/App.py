import json
import traceback
from flask import Flask, request,jsonify, Response
from flask_socketio import SocketIO, emit
from backend.agents.planner import Planner
from backend.agents.retriever import Retreiver
from backend.agents.executor import Executor
from backend.ingestion.ingest import Ingestor


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/query", methods=["POST"])
def query_api():
    data = request.json
    query = data["query"]
    print("--debug payload recieved------", data)


    planner = Planner()
    retriever = Retreiver()
    executor = Executor()

    def stream():
        yield json.dumps({"event": "Planning query"}) + "\n"
        plan = planner._create_plan(query)

        yield json.dumps({"event": "Retrieving enterprise knowledge"}) + "\n"
        docs = retriever._retrieve(query, plan)

        yield json.dumps({"event": "Synthesizing grounded answer"}) + "\n"

        for token in executor._stream_synthesis(query, docs,socketio):
            yield json.dumps({"token": token}) + "\n"

        yield json.dumps({"event": "Finalizing response"}) + "\n"

    return Response(stream(), mimetype="application/json")

# @app.route("/query", methods=["POST"])
# def query_api_v1():
#     data = request.json
#     print("--debug payload recieved------", data)
#     query = data["query"]

#     planner = Planner()
#     retriever = Retreiver()
#     executor = Executor()

#     plan = planner._create_plan(query)
#     docs = retriever._retrieve(query, plan)
#     answer = executor._execute_synthesis(query, docs)

#     return jsonify({
#         "answer": answer,
#         "sources": docs
#     })



# Streamlit is optimized for stateless reruns. For reliability and demo safety, 
# I exposed a REST boundary while retaining Socket.IO internally for future streaming clients

# @socketio.on("query")
# def handle_query(data):
#     query = data["query"]

#     planner = Planner()
#     retriever = Retreiver()
#     executor = Executor()

#     socketio.emit("agent_event", {"stage": "Planning query"})
#     plan = planner._create_plan(query)

#     socketio.emit("agent_event", {"stage": "Retrieving enterprise knowledge"})
#     docs = retriever._retrieve(query, plan)

#     executor._stream_synthesis(query, docs, socketio)



if __name__ == "__main__":
    ingestor = Ingestor(texts=[], meta=[])
    ingestor.ingest_docs()

    print("Documents loaded into memory", ingestor.texts[:200], ingestor.meta)
    socketio.run(app, port=5000)
