import os
from dotenv import load_dotenv

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from countdown import Countdown
from datetime import datetime

load_dotenv()
mode = os.getenv("MODE")
TOKEN = os.getenv("TOKEN")

# List of available commands
# hype_level - Show the level of hype
# days_left - Days before the next trip
# hype_level_ru - Показать уровень хайпа до следующего события
# days_left_ru - Показать количество дней до следующего события

def hype_level_en(bot, update):
  chat_id = update.message.chat_id

  bot.send_message(chat_id=chat_id, text='Hype!!!!!!!')

def days_left_en(bot, update):
  chat_id = update.message.chat_id

  countdown = Countdown(next_event(), 'en')
  bot.send_message(chat_id=chat_id, text=countdown.message())

def hype_level_ru(bot, update):
  chat_id = update.message.chat_id

  bot.send_message(chat_id=chat_id, text='Хайп!!!!!!!')

def days_left_ru(bot, update):
  chat_id = update.message.chat_id

  countdown = Countdown(next_event(), 'ru')
  bot.send_message(chat_id=chat_id, text=countdown.message())

def next_event():
  return datetime(2019, 8, 13, 7, 0)

if mode == "prod":
  def run(updater):
    PORT = int(os.environ.get("PORT", "8443"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
else:
  def run(updater):
    updater.start_polling()
    updater.idle()

def main():
  updater = Updater(TOKEN)

  dp = updater.dispatcher
  dp.add_handler(CommandHandler('hype_level', hype_level_en))
  dp.add_handler(CommandHandler('days_left', days_left_en))
  dp.add_handler(CommandHandler('hype_level_ru', hype_level_ru))
  dp.add_handler(CommandHandler('days_left_ru', days_left_ru))

  run(updater)

if __name__ == '__main__':
  main()
