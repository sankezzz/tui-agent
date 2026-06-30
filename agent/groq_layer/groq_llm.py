from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=groq_api_key,
)

def chatGroq(user_prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            # Set an optional system message. This sets the behavior of the
            # assistant and can be used to provide specific instructions for
            # how it should behave throughout the conversation.
            {
                "role": "system",
                "content": "You are a personal code assistant for me you will help me with various things in ongoing projects you will guide me as a senior and will provide code with the proper short explantion"
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": user_prompt,
            }
        ],

        # The language model which will generate the completion.
        model="qwen/qwen3-32b"
    )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content


