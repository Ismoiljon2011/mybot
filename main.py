from config import *
from users import *
from keyboard import *
from callback import *

from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from asyncio import run


dp = Dispatcher()
bot = Bot(token=TOKEN)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        f"Salom {message.from_user.first_name}.\nIsmoiljonning ovoz berish botiga hushkelibsiz.\nOvoz berish uchun /voice komandasini yuboring."
    )


@dp.message(Command("voice"))
async def voice(message: Message):
    a = open("users.txt", "r").readlines()
    s = open("data.txt", "r").readlines()
    Id = message.from_user.id
    if str(Id) not in a or Id == ADMIN_ID:
        await message.answer(
            f"Ismoiljon: {s[0].strip()} ta ovoz\nIzzatbek: {s[1].strip()} ta ovoz\n\nOvoz berish uchun pastdagi nomzotlardan birini tanlang.",
            reply_markup=inline,
        )
        if not Id == ADMIN_ID:
            with open("users.txt", "a") as f:
                f.write(f"\n{str(Id)}")
    else:
        await message.answer("Siz ovoz bergansiz")


@dp.message(Command("view"))
async def view(message: Message):
    a = open("data.txt", "r").readlines()
    await message.answer(
        f"Ismoiljon: {a[0].strip()} ta ovoz\nIzzatbek: {a[1].strip()} ta ovoz"
    )


async def main():
    dp.callback_query.register(ismoiljonVoice, F.data == "ismoiljon")
    dp.callback_query.register(izzatbekVoice, F.data == "izzatbek")
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Botni ishga tushurish"),
            BotCommand(command="voice", description="Ovoz berish"),
            BotCommand(command="view", description="Ovozlar sonini ko'rish"),
        ]
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print("Bot ishga tushdi")
        run(main())
    except KeyboardInterrupt:
        print("Bot tuxtadi")
