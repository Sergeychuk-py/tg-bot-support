from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def markup():
    keyboards = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🆘 Поддержка", callback_data="support")],
        [InlineKeyboardButton(text="🤖 Заказать разработку", callback_data="order")],
        [InlineKeyboardButton(text='📢 Наша группа ВК', url="https://vk.com/telegabots72")]
    ], resize_keyboard=True)
    return keyboards