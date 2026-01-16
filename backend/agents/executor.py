import time
import traceback
from utils.llm import call_llm

class Executor:

    def __init__(self):
        pass

    def _execute_synthesis(self,query:str,docs:list):
        """Execute method"""
     
        context = "\n".join(
            [f"[{i}] {d['content']}" for i, d in enumerate(docs)]
        )

        prompt = f"""
            You are an enterprise assistant.
            Answer ONLY using the sources below.
            Cite using [index]. If insufficient info, say so.

            Question: {query}

            Sources:
            {context}
            """

        return call_llm(prompt)
