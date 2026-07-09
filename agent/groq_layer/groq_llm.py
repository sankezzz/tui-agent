from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=groq_api_key,
)


def chatGroq(history):
    chat_completion = client.chat.completions.create(
        include_reasoning=False,
        messages=[
            # Set an optional system message. This sets the behavior of the
            # assistant and can be used to provide specific instructions for
            # how it should behave throughout the conversation.
            {
                "role": "system",
                "content": "You are a personal code assistant for me you will help me with various things in ongoing projects you will guide me as a senior and will provide code with the proper short explantion -- give code directly no bs at all mostly be clear precise ",
            },
            # Set a user message for the assistant to respond to.
            *history
        ],

        # The language model which will generate the completion.
        model="qwen/qwen3-32b"
    )
    return chat_completion.choices[0].message.content


