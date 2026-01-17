import os
from ollama import chat




def call_ollama(messages, model="gemma3:1b"):
    response = chat(
        model=model,
        messages=messages
    )
    return response.message.content



def stream_ollama(messages, model="gemma3:1b"):
    response = chat(
        model=model,
        messages=messages,
        stream=True
    )

    for chunk in response:
        if "message" in chunk and "content" in chunk["message"]:
            yield chunk["message"]["content"]



