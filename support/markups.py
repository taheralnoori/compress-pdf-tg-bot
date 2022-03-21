from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('دعم 💊', url='https://t.me/engineering_electrical9/719?comment=1'),
            InlineKeyboardButton('👨🏻‍💻 مطور', url='https://t.me/ta_ja199')
        ]
        ]

close = [
        [
            InlineKeyboardButton('دعم 💊', url='https://t.me/engineering_electrical9/719?comment=1'),
            InlineKeyboardButton('أغلق ❌', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
