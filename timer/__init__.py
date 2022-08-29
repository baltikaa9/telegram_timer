import asyncio

from aiogram import types

from bot import bot


async def set_timer(message: types.Message, time):
    await bot.send_message(message.chat.id, f'Поставлен таймер на <b>{time}</b> секунд', parse_mode='html')
    bot_message = await bot.send_message(message.chat.id, f'Осталось {time} сек.')
    for time_left in range(time - 1, -1, -1):
        await asyncio.sleep(1)
        await bot_message.edit_text(f'Осталось {time_left} сек.')
    await bot_message.delete()
    await bot.send_message(message.chat.id, f'Ваш таймер на {time} секунд закончился')