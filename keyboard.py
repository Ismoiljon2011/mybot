from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ismoiljon", callback_data="ismoiljon"),
            InlineKeyboardButton(text="Izzatek", callback_data="izzatbek"),
        ]
    ]
)
