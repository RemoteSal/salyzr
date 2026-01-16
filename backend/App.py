from flask import Flask
from flask_socketio import SocketIO, emit
from backend.agents.planner import Planner
from agents.retriever import Retreiver
from agents.executor import Executor

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("query")
def handle_query(data):
    query = data["query"]
    planner = Planner()
    retreiver = Retreiver()
    executor = Executor()

    emit("status", {"msg": "Planning search"})
    plan = planner._create_plan(query)
    print("--debug plan-----", plan)

    emit("status", {"msg": "Retrieving enterprise knowledge"})
    docs = (query, plan)

    emit("status", {"msg": "Generating grounded answer"})
    answer = executor._execute_synthesis(query, docs)
    print("--debug response-----", answer)
    
    emit("response", {"answer": answer, "sources": docs})

if __name__ == "__main__":
    socketio.run(app, port=5000)
