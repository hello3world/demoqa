from langchain.chat_models import ChatOpenAI 
from browser_use import Agent 
import asyncio
from dotenv import load_dotenv 

load_dotenv()

async def main():
    llm = ChatOpenAI(model_name="gpt-4")
    task = """Открой Хабр (habr.com)"""
    agent = Agent(
        task=task,
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())