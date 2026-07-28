import asyncio
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz

# === ВАШИ НАСТРОЙКИ ===
BOT_TOKEN = "8720877897:AAGoOuv_j54-wRSErmKDN88CTLzYDe3YIms"

# Вставьте сюда ID вашей группы (число с минусом, например: -100123456789)
GROUP_CHAT_ID = -5498910232  

# Часовой пояс
TIMEZONE = "Europe/Moscow"    

# Ваш список привычек
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

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler(timezone=pytz.timezone(TIMEZONE))

# Функция отправки сообщения
async def send_morning_habits():
    await bot.send_message(
        chat_id=GROUP_CHAT_ID, 
        text=HABITS_TEXT
    )

async def main():
    # Настройка отправки каждый день ровно в 06:00
    scheduler.add_job(send_morning_habits, 'cron', hour=6, minute=0)
    scheduler.start()
    
    print("Бот levelup (@horikgks_bot) успешно запущен и ожидает 06:00...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())