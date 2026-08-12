import asyncio
from datetime import datetime, date
from zoneinfo import ZoneInfo
from aiogram import Bot

# Твой токен
BOT_TOKEN = "8720877897:AAGoOuv_j54-wRSErmKDN88CTLzYDe3YIms"

# Твой ID группы
GROUP_CHAT_ID = -5498910232  

# 🗓 ДАТА СТАРТА ЧЕЛЛЕНДЖА: (Год, Месяц, День)
START_DATE = date(2026, 7, 25)

def get_message_text():
    today = datetime.now(ZoneInfo("Europe/Moscow")).date()
    
    day_count = (today - START_DATE).days + 1
    if day_count < 1:
        day_count = 1

    return f"""Доброе утро!! ☀️ День {day_count}
С каждым днём ближе к цели 🪬🤍

[Арина]
every day 
1. Массаж лица 💆🏻‍♀️
2. Йога 🧘🏻‍♀️🪷
3. Английский 🇺🇸📚
4. 10k шагов/приседания
weekend
1. Дизайн 4 pj 👩🏻‍💻
2. Силовые тренировки

[Лера]
every day 
1. Массаж лица 💆🏼‍♀️
2. Упр на глаз 👁💪🏼
3. Молчание/медитация 🔇🤫
4. Йога 🧘🏼‍♀️🪷
5. Записывать состояние и события дня в «здоровье»
weekend 
1. Английский (2-3 раза)🇺🇸📚
2. Тренировка (2-3 раза)🏃🏼‍♀️💪🏼
3. Самопрограммирование /  выписать мысли (1 раз в неделю)"""

async def main():
    bot = Bot(token=BOT_TOKEN)
    try:
        await bot.send_message(chat_id=GROUP_CHAT_ID, text=get_message_text())
    finally:
        await bot.session.close()

if name == "__main__":
    asyncio.run(main())
