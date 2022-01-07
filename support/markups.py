from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('Support', url='https://t.me/Dsrs_Group'),
            InlineKeyboardButton('DEVLOPER', url='https://t.me/kashmir_1')
        ]
        ]

close = [
        [
            InlineKeyboardButton('Support', url='https://t.me/Dsrs_Group'),
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
