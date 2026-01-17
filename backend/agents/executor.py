import time
import traceback
from backend.utils.llm import call_ollama

class Executor:

    def __init__(self):
        pass

    def _execute_synthesis(self,query:str,docs:list):
        """Execute method"""

        try:
     
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

            response = call_ollama(prompt)
            print("--debug response------", response)

        except Exception as e:
            print("--debug _execute_synthesis error :", str(e), traceback.format_exc())
