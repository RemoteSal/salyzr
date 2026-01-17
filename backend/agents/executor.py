import time
import traceback
from backend.utils.llm import call_ollama, stream_ollama
from backend.utils.prompts import PromptFormatter

class Executor:

    def __init__(self):
        self.memory = ""

    ## for normal llm call without streaming
    def _execute_synthesis(self,query:str,docs:list):
        """Execute method"""

        try:
     
            prompt_builder = PromptFormatter(memory=self.memory)
            messages = prompt_builder.build_messages(query, docs)

            # print("\n---debug formatted promptmsg-------", messages)
            response = call_ollama(messages)

            print("\n--debug _execute_synthesis_response------", response)
            return response

        except Exception as e:
            print("--debug _execute_synthesis error :", str(e), traceback.format_exc())


    def _stream_synthesis(self, query, docs, socketio):
        prompt = PromptFormatter()
        messages = prompt.build_messages(query, docs)

        socketio.emit("agent_event", {"stage": "Synthesizing grounded answer"})

        final_answer = ""
        try:
            for token in stream_ollama(messages):
                final_answer += token
                socketio.emit("answer_chunk", {
                    "token": token
                })

            socketio.emit("agent_event", {"stage": "Finalizing response"})
            print("--debug _stream_synthesis ans: ", final_answer)

            return final_answer
        except Exception as e:
            print("--debug _stream_synthesis error :", str(e), traceback.format_exc())


