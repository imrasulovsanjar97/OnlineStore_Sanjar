from aiogram import Router, F
from aiogram.types import Message
from aiogram import Dispatcher, types

from config import DB_NAME
from keyboards.all_keyboards import get_categories, kb_start
from utils.database import Database

db = Database(DB_NAME)
message_router = Router()
dp = Dispatcher()

@message_router.message(F.text == 'Categories')
async def category_handler(message: Message):
    await message.answer(
        text="Select category, please...",
        reply_markup=get_categories()
    )

@message_router.message(F.text.in_({'Smartphones', 'Notebooks', 'Printers', 'Monitors'}))
async def product_handler(message: Message):
    cats = db.get_categories()
    for cat in cats:
        if message.text == cat[1]:
            products = db.get_products(cat[0])
            
   
    for product in products[:len(products)]:  
        await message.answer_photo(
            photo=product[4],  
            caption=f"<b>{product[1]}:</b>\n\n{product[3]}"  
        )

