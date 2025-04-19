import chainlit as cl
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from typing import Optional
from src.config import instruction
from src.llm import ChatOpenRouter, ask_bot

load_dotenv()
import os

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# def ask_bot(user_message:str):
    
#     llm = ChatOpenRouter(
#     model_name="deepseek/deepseek-chat-v3-0324:free",
#     openai_api_key=GOOGLE_API_KEY
#             )
    
#     messages =[{"role": "system", "content": instruction},
#              {"role": "user", "content": user_message}]

#     response= llm.invoke(messages)
  
#     return response


@cl.on_message
async def main(user_message: cl.Message):
    # Your custom logic goes here...
    
    response= ask_bot(user_message.content)

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {response.content}"
    ).send()


# if __name__ == "__main__":
#     print("Bot: Hi there! How can I help you?")
#     result=ask_bot("What is the prise of pizza")
#     print(result)