import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from typing import Optional
from src.config import instruction

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

class ChatOpenRouter(ChatOpenAI):
    openai_api_base: str
    openai_api_key: str
    model_name: str

    def __init__(self,
                 model_name: str,
                 openai_api_key: Optional[str] = None,
                 openai_api_base: str = "https://openrouter.ai/api/v1",
                 **kwargs):
        openai_api_key = openai_api_key or os.getenv('OPENROUTER_API_KEY')
        super().__init__(openai_api_base=openai_api_base,
                         openai_api_key=openai_api_key,
                         model_name=model_name, **kwargs)
        
llm = ChatOpenRouter(
    model_name="google/gemini-2.5-pro-exp-03-25:free",
    openai_api_key=GOOGLE_API_KEY
            )

def ask_bot(user_message:str):
    
    llm = ChatOpenRouter(
    model_name="deepseek/deepseek-chat-v3-0324:free",
    openai_api_key=GOOGLE_API_KEY
            )
    
    messages =[{"role": "system", "content": instruction},
             {"role": "user", "content": user_message}]

    response= llm.invoke(messages)
  
    return response

if __name__ == "__main__":
    print("Bot: Hi there! How can I help you?")
    message=ask_bot("What is the capital of India?")
    print(message)