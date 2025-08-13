# In llm_bot.py
import openai
import os

def get_openai_response(prompt, history):
    openai.api_type = "azure"
    openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
    openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
    openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

    messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
    for role, content in history:
        messages.append({"role": role, "content": content})
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        engine=os.getenv("AZURE_OPENAI_MODEL_NAME"),
        messages=messages
    )
    return response.choices[0].message.content
