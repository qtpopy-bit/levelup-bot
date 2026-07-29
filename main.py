import asyncio
from aiogram import Bot

# Твой токен
BOT_TOKEN = "8720877897:AAGoOuv_j54-wRSErmKDN88CTLzYDe3YIms"

# Твой ID группы (обязательно проверь, что тут минус и правильные цифры!)
GROUP_CHAT_ID = -5498910232  

HABITS_TEXT = (
    "Доброе утро!! ☀️\n"
    "С каждым днём ближе к цели 🪬🤍\n\n"
    "[Арина]\n"
    "1. Массаж лица 💆🏻‍♀️\n"
    "2. Йога 🧘🏻‍♀️🪷\n"
    "3. Английский 🇺🇸📚\n"
    "4. Молчание 🔇🤫\n\n"
    "[Лера]\n"
    "1. Массаж лица 💆🏼‍♀️\n"
    "2. Упр на глаз 👁️💪🏼\n"
    "3. Молчание 🔇🤫"
)

async def main():
    bot = Bot(token=BOT_TOKEN)
    try:
        await bot.send_message(chat_id=GROUP_CHAT_ID, text=HABITS_TEXT)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
