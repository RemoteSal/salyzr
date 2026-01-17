import os
from ollama import chat

# from openai import OpenAI
# from dotenv import load_dotenv
# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_ollama(messages, model="gemma3:1b"):
    response = chat(
        model=model,
        messages=messages
    )
    return response.message.content




# def call_llm(prompt: str) -> str:
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0
#     )
#     return response.choices[0].message.content
