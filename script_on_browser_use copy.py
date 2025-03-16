from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext
import asyncio
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from browser_use import Agent

load_dotenv()

browser = Browser(
    config=BrowserConfig(
        headless=False,
        chrome_instance_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    )
)

controller = Controller()

async def main():
    llm = ChatOpenAI(model_name="gpt-4o")
    task = """Открой Хабр (habr.com), найди какую-нибудь статью от юзера ElKornacio, открой её полную версию,
    и предложи вариант токсичного комментария на русском, связанного с этой статьёй, после опубликуй этот комментарий к статье"""
    
    agent = Agent(
        task=task,
        llm=llm,
        controller=controller,
        browser=browser,
    )
    
    result = await agent.run()
    print(result)

asyncio.run(main())
