from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import DB_NAME
from utils.database import Database

db = Database(DB_NAME)

kb_start = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Categories')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Please, press button...',
    one_time_keyboard=True
)

def get_categories() -> ReplyKeyboardMarkup:
        categories = db.get_categories()
        cats = []
        for cat in categories:
            cats.append(
                KeyboardButton(text=cat[1])
            )
        markup = ReplyKeyboardMarkup(
            keyboard=[cats],
            resize_keyboard=True,
            input_field_placeholder='Please, select a category...',
            one_time_keyboard=True
        )
        return markup
        
        
        
