from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import Bot, Router, F, types
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from data.orm_query import create_question, create_answer
from keyboards import markup

router_handlers = Router()


@router_handlers.message(CommandStart("start"))
async def start(message: types.Message):
    await message.answer(f"Здраствуйте 👋 {message.from_user.full_name}"
                         , reply_markup=markup())


@router_handlers.callback_query(F.data == "support")
async def start(callback: CallbackQuery, bot: Bot):
    await callback.message.answer(f"Здраствуйте {callback.message.from_user.full_name} какой у вас вопрос?")
    await bot.send_message(chat_id=1526741555, text=callback.message.text)


@router_handlers.message((F.text) & (F.chat.id != 1526741555))
async def question(message: types.Message, session: AsyncSession, bot: Bot):
    await create_question(message.chat.id, message.text, session)
    await bot.send_message(chat_id=1526741555, text=message.text)
    await message.answer('<i>Сообщение отправлено</i>', parse_mode=ParseMode.HTML)


@router_handlers.message((F.reply_to_message) & (F.chat.id == 1526741555))
async def answer(message: types.Message, session, bot: Bot):
    chat_id = await create_answer(message.reply_to_message.text, session)
    await bot.send_message(chat_id=chat_id, text=f"<b>Ответ от техподдержки:</b>\n{message.text}",
                           parse_mode=ParseMode.HTML)
    await message.answer('<i>Ответ отправлен</i>', parse_mode=ParseMode.HTML)
