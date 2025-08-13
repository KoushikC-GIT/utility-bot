import os
import sys
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

def get_utility_bot_response(prompt_text):
    """
    Sends a prompt to Azure OpenAI and returns the response.
    """
    try:
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_MODEL_NAME"),  # Use your deployment name here
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt_text}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"

# main
if __name__ == "__main__":

    while True:

        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            break
        
        response = get_utility_bot_response(user_input)
        print(f"Agent: {response}")
        