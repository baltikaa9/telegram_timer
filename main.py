from aiogram import Bot, executor, Dispatcher

from bot import bot
from config import *
from inline_buttons import *
from stopwatch_control import *
from timer import *


dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(text='Секундомер')
    markup.add(btn)
    await message.answer('Для запуска таймера введите время в секундах :)', reply_markup=markup)


@dp.message_handler()
async def timer(message: types.Message):
    # Таймер
    if message.text.isdigit():
        time = int(message.text)
        await set_timer(message, time)

    # Секундомер
    if message.text.lower() == 'секундомер':
        await message.delete()
        if message.chat.id not in chat_id:
            await start_stopwatch(message, stop_markup, continue_markup)


@dp.callback_query_handler()
async def some_callback_handler(callback_query: types.CallbackQuery):
    if callback_query.data == 'stop':
        await stop_stopwatch(callback_query.message)
    if callback_query.data == 'continue':
        await continue_stopwatch(callback_query.message)
    if callback_query.data == 'del':
        await delete_stopwatch(callback_query.message)
    await bot.answer_callback_query(callback_query.id)


if __name__ == '__main__':
    executor.start_polling(dp)
