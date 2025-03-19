from aiogram.types import CallbackQuery
from users import save_voice,ismoiljon,izzatbek

async def ismoiljonVoice(cData:CallbackQuery):
    await cData.message.edit_text(text="Siz Ismoiljonga ovoz berdingiz.\nOvoz berganingiz uchun raxmat.")
    global ismoiljon
    ismoiljon+=1
    save_voice(ismoiljon,izzatbek)


async def izzatbekVoice(cData:CallbackQuery):
    await cData.message.edit_text(text="Siz Izzatbekga ovoz berdingiz.\nOvoz berganingiz uchun raxmat.")
    global izzatbek
    izzatbek+=1
    save_voice(ismoiljon,izzatbek)