from aiogram import Router, types, Bot, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.enums import ParseMode

fms_router = Router()


class Reg(StatesGroup):
    name = State()
    description = State()
    number = State()


@fms_router.callback_query(F.data == "order")
async def order_name(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg.name)
    await callback.message.answer('Здравствуйте👋, как я могу к вам обращаться?')


@fms_router.message(Reg.name)
async def order_description(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.description)
    await message.answer('🗒 Опишите задачи бота и его функционал')


@fms_router.message(Reg.description)
async def order_number(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(Reg.number)
    await message.answer('📞 Введите ваш номер телефона,\n привязаного к телеграму')


@fms_router.message(Reg.number)
async def order_number(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f"🤵  ️Имя: {data['name']}\n\n📞 Телефон: {data['number']}\n\n🗒 Описание задачи: {data['description']}\n------------------------------------------\n<b>Спасибо, заявка принята ✅</b>\nСкоро с вами свяжутся👌\n",
                         parse_mode=ParseMode.HTML)
    await state.clear()
    await bot.send_message(chat_id=1526741555, text=f"<b>Заявка</b>\nИмя:{data['name']}\nТелефон:{data['number']}\nОписание задачи:{data['description']}", parse_mode=ParseMode.HTML)
