from aiogram import types

stop_markup = types.InlineKeyboardMarkup()
continue_markup = types.InlineKeyboardMarkup()

btn_stop = types.InlineKeyboardButton(text='Стоп', callback_data='stop')
btn_continue = types.InlineKeyboardButton(text='Продолжить', callback_data='continue')
btn_del = types.InlineKeyboardButton(text='Удалить', callback_data='del')

stop_markup.add(btn_stop, btn_del)
continue_markup.add(btn_continue, btn_del)
