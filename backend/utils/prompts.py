# backend/prompts/synthesis.py
from typing import List, Dict

class PromptFormatter:
    """
    Responsible for formatting enterprise Q&A prompts into LLM-compatible messages.
    """

    SYSTEM_PROMPT = (
        "You are an enterprise intelligence assistant.\n"
        "Answer using the provided sources.\n"
        "Cite facts using [index].\n"
        "Give a strucuted answer and detailed one for the user query."
    )

    def __init__(self, memory: List[Dict] | None = None):
        self.memory = memory or []

    def _format_context(self, docs: List[Dict]) -> str:
        if not docs:
            result =  "No relevant enterprise documents were found."

        result= "\n".join(
            f"[{i}] {doc['content']}"
            for i, doc in enumerate(docs)
        )
        # print("--debug _format_context res-----", result)
        return result

    def build_messages(self, query: str, docs: List[Dict]) -> List[Dict]:
        context = self._format_context(docs)

        return [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            *self.memory,
            {
                "role": "user",
                "content": (
                    f"Question:\n{query}\n\n"
                    f"Sources:\n{context}"
                )
            }
        ]


