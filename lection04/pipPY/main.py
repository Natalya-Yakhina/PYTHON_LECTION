# python3 -m venv .folder название папки где будут все скаченные библиотеки
# -------------------------------------------------------------------------
#                   isOdd - проверка числа на четность

# from isOdd import isOdd
# print(isOdd(0)) #//=> false
# print(isOdd(4)) #//=> false
# -------------------------------------------------------------------------
#             progress - библиотека прогресс бара(процесс чтения)

# from progress.bar import Bar
# import time # иммитатор загрузки
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1) # задержка
#     # Do some work
#     bar.next()
# bar.finish()
# -------------------------------------------------------------------------
#                     emoji - библиотека смайлов

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# -------------------------------------------------------------------------
#         matplotlib - нарисовать график математической функции

# import matplotlib.pyplot as plt
# import numpy as np
# plt.style.use('_mpl-gallery')
# # make data:
# np.random.seed(3)
# x = 0.5 + np.arange(8)
# y = np.random.uniform(2, 7, len(x))
# # plot
# fig, ax = plt.subplots()
# ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# lisdt = [1,2,3,2,7]
# plt.plot(list)
# plt.show()
# -------------------------------------------------------------------------
#                              СОЗДАНИЕ БОТА

# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# app = ApplicationBuilder().token("5783314859:AAH0yxtMbSfflc03SxZaxamMhOZoV_RjKr8").build()

# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()