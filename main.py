import asyncio
from datetime import datetime, date
from zoneinfo import ZoneInfo
from aiogram import Bot

# Твой токен
BOT_TOKEN = "8720877897:AAGoOuv_j54-wRSErmKDN88CTLzYDe3YIms"

# Твой ID группы
GROUP_CHAT_ID = -5498910232  

# 🗓 ДАТА СТАРТА ЧЕЛЛЕНДЖА: (Год, Месяц, День)
# Дата 22 августа 2026 года даёт ровно День 75 на сегодня:
START_DATE = date(2026, 8, 22)

def get_message_text():
    today = datetime.now(ZoneInfo("Europe/Moscow")).date()
    
    day_count = (today - START_DATE).days + 1
    if day_count < 1:
        day_count = 1

    return f"""Доброе утро!! ☀️ День {day_count}
С каждым днём ближе к цели 🪬🤍

[Арина]
every day 
1. Йога 🧘🏻‍♀️🪷
2. Английский 🇺🇸📚
3. Планирование 📋✍🏻
weekend
1. Чтение 3 часа 📖☕️
2. Тренировка (2 раза в неделю) 🏃🏻‍♀️💪🏼
3. Минимум 2 видео в неделю 🎬📱
4. Составление плана питания 🥗🥑

[Лера]
every day 
1. Упр на глаз 👁💪🏼
2. Молчание/медитация 🔇🤫
3. Йога 🧘🏼‍♀️🪷
weekend
1. Английский (2-3 раза)🇺🇸📚
2. Тренировка (2-3 раза)🏃🏼‍♀️💪🏼"""

async def main():
    bot = Bot(token=BOT_TOKEN)
    try:
        await bot.send_message(chat_id=GROUP_CHAT_ID, text=get_message_text())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
