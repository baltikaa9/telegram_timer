import asyncio
from datetime import datetime

from aiogram import types
from aiogram.utils import exceptions

from config import chat_id
from bot import bot


async def start_stopwatch(message: types.Message, stop_markup, continue_markup):
    temp = 75600  # 1970-01-02 00:00:00
    bot_message = await bot.send_message(message.chat.id, f'{datetime.fromtimestamp(temp).strftime("%H:%M:%S")}',
                                         reply_markup=stop_markup)
    # global message_id
    chat_id[message.chat.id] = True
    await asyncio.sleep(1)
    while chat_id.get(message.chat.id, False):
        try:
            # btn_markup.add(btn_stop, btn_del)
            temp += 1
            await bot_message.edit_text(f'{datetime.fromtimestamp(temp).strftime("%H:%M:%S")}',
                                        reply_markup=stop_markup)
            await asyncio.sleep(1)
            if not chat_id.get(message.chat.id, False):
                await bot_message.edit_text(f'{datetime.fromtimestamp(temp).strftime("%H:%M:%S")}',
                                            reply_markup=continue_markup)
            while not chat_id.get(message.chat.id, False):
                await asyncio.sleep(0.1)
                # btn_markup.insert(btn_continue)
        except exceptions.MessageToEditNotFound:
            break


async def stop_stopwatch(message: types.Message):
    chat_id[message.chat.id] = False
    # stopwatch_flag = False


async def continue_stopwatch(message: types.Message):
    # global stopwatch_flag
    chat_id[message.chat.id] = True


async def delete_stopwatch(message: types.Message):
    await message.delete()
    try:
        chat_id.pop(message.chat.id)
    except KeyError:
        pass