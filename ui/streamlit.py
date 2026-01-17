import streamlit as st
import requests
import json

st.set_page_config(page_title="Enterprise Search", layout="wide")
st.title("Enterprise Intelligence Search")

query = st.text_input("Ask a question about your enterprise")

if st.button("Search") and query:
    st.subheader("Agent Timeline")
    timeline_placeholder = st.empty()

    st.subheader("Answer")
    answer_placeholder = st.empty()

    events = []
    answer = ""

    with st.spinner("Querying enterprise knowledge..."):
        with requests.post(
            "http://127.0.0.1:5000/query",
            json={"query": query},
            stream=True,
        ) as res:
            # print(json.loads(res))

            for line in res.iter_lines():
                if not line:
                    continue

                payload = json.loads(line.decode())

                if "event" in payload:
                    events.append(payload["event"])
                    # timeline_placeholder.markdown(
                    #     "\n".join([f"• {e}" for e in events])
                    # )
                    timeline_placeholder.markdown(
                        "\n".join([f"✅ {e}\n\n" for e in events])
                    )


                if "token" in payload:
                    answer += payload["token"]
                    # answer_placeholder.markdown(answer)
                    answer_placeholder.markdown(answer + "▌")

