import streamlit as st
import socketio

st.set_page_config(page_title="Enterprise Search", layout="wide")

sio = socketio.Client()
sio.connect("http://localhost:5000")

st.title("Enterprise Intelligence Search")

query = st.text_input("Ask a question about your enterprise")

if st.button("Search"):
    sio.emit("query", {"query": query})

@sio.on("status")
def on_status(data):
    st.info(data["msg"])

@sio.on("response")
def on_response(data):
    st.success(data["answer"])
    st.subheader("Sources")
    for s in data["sources"]:
        st.write(f"- {s['source']}")
