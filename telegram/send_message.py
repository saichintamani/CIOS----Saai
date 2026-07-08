import asyncio
import os

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def main():
    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text="🚀 CIOS Started Successfully!"
    )

    print("Message sent successfully.")

if __name__ == "__main__":
    asyncio.run(main())