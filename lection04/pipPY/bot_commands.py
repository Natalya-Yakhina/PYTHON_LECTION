# понадобятся библиотеки для работы
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context) # переходить от одной команды к другой
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text # сообщение пользователя
    print(msg)
    items = msg.split() # разобрать сообщение /sum 123 3434
    x = int(items[1])
    y = int(items[2])
    # внештатные ситуации описываем здесь, вдруг нет элемента

    await update.message.reply_text(f'{x} + {y} = {x + y}')

# def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     log(update, context)
#     # update.message.reply_text(f'Hi {update.effective_user.first_name}!')