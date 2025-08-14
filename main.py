from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import asyncio

# 🔑 Токен бота
TOKEN = ""

# 🆔 ID користувача, якому бот пересилає всі повідомлення
FORWARD_TO_USER_ID =   # ← встав свій Telegram user_id

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Хендлер для всіх повідомлень
@dp.message()
async def forward_all_messages(message: Message):
    # Отримаємо username або сформуємо посилання
    user = message.from_user
    if user.username:
        user_link = f"@{user.username}"
    else:
        user_link = f'<a href="tg://user?id={user.id}">[Користувач без username]</a>'

    # Сформуємо текст перед повідомленням
    header = f"📩 Повідомлення від {user_link}:"

    # Надсилаємо повідомлення з підписом
    await bot.send_message(FORWARD_TO_USER_ID, header, parse_mode="HTML")
    await message.copy_to(FORWARD_TO_USER_ID)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
