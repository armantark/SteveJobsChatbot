import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from a .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=OPENAI_API_KEY)

# Predefined messages to set the context for the chatbot
messages_so_far = [
    {
        "role": "system",
        "content": (
            "You are Steve Jobs, world-renowned CEO of Apple. "
            "Adopt his speech patterns as closely as possible in your responses. "
            "Try to emulate his snarky but inspirational speech style."
            # Additional instructions can be added here if needed.
        )
    }
]


def continue_chat(user_query):
    """
    Continues the chat conversation based on the user's input.

    This function appends the user's query to the ongoing conversation, gets a response from the OpenAI chat model,
    and then appends that response to the conversation.

    Args:
        user_query (str): The user's input text to the chatbot.

    Returns:
        str: The chatbot's (OpenAI's) response to the user's query.
    """

    # Append the user's query to the conversation history
    messages_so_far.append({"role": "user", "content": user_query})

    # Get the chatbot's response using OpenAI's chat completion
    chat_completion = client.chat.completions.create(
        messages=messages_so_far,
        model="gpt-3.5-turbo",
    )
    response = chat_completion.choices[0].message.content

    # Append the chatbot's response to the conversation history
    messages_so_far.append({"role": "assistant", "content": response})

    # Optional: Print the conversation history (for debugging or logging)
    print(messages_so_far)

    return response
