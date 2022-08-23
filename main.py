import asyncio
import os
from aiogram import Bot, executor, Dispatcher

bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler()
async def timer(message):
    try:
        time = int(message.text)
        if time < 0:
            raise ValueError

        await bot.send_message(message.chat.id, f'Поставлен таймер на <b>{time}</b> секунд', parse_mode='html')
        bot_message = await bot.send_message(message.chat.id, f'Осталось {time} сек.')
        for time_left in range(time - 1, -1, -1):
            await asyncio.sleep(1)
            await bot_message.edit_text(f'Осталось {time_left} сек.')
        await bot.send_message(message.chat.id, f'Ваш таймер на {time} секунд закончился')
    except (TypeError, ValueError):
        await bot.send_message(message.chat.id, 'Введите корректное время')


if __name__ == '__main__':
    executor.start_polling(dp)
