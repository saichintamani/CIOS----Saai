import asyncio
import os

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


async def send_daily_report():

    bot = Bot(token=BOT_TOKEN)

    report = """
🔥 CIOS DAILY REPORT

GitHub Status: SAFE ✅

Top Project:
CIOS----Saai

Priority Project:
Lumina-

Recommended Task:
Design System Architecture

Impact:
HIGH

Estimated Time:
45 Minutes
"""

    await bot.send_message(
        chat_id=CHAT_ID,
        text=report
    )

    print("Daily report sent successfully.")


if __name__ == "__main__":
    asyncio.run(send_daily_report())