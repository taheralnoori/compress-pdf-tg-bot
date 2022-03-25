from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('دعم 💊', url='https://t.me/engineering_electrical9/719?comment=1'),
            InlineKeyboardButton('👨🏻‍💻 مطور', url='https://t.me/ta_ja199')
        ],
        [   InlineKeyboardButton('🌟تقييم البوت🌟', url='https://t.me/tlgrmcbot?start=compresspdfbot-review')
        ]
        ]

close = [
        [
            InlineKeyboardButton('دعم 💊', url='https://t.me/engineering_electrical9/719?comment=1'),
            InlineKeyboardButton('👨🏻‍💻 مطور', url='https://t.me/ta_ja199')
        ],
        [   InlineKeyboardButton('🌟تقييم البوت🌟', url='https://t.me/tlgrmcbot?start=compresspdfbot-review')
        ]
        ]


start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
