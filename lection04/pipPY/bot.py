#                              СОЗДАНИЕ БОТА

# exec(open('C:\Users\User\Desktop\lection\python_lection\lection04\pipPY\lection04\pipPY\.folder\bot.py').read())

import imp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5783314859:AAH0yxtMbSfflc03SxZaxamMhOZoV_RjKr8").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')
app.run_polling()