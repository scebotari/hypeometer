import os
from dotenv import load_dotenv
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from datetime import datetime

from utils.countdown import Countdown
from hypeometer.hypeometer import Hypeometer
from responders.days_left import DaysLeft
from locales.configs import set_locale

load_dotenv()
mode = os.getenv("MODE")
TOKEN = os.getenv("TOKEN")

# List of available commands
# hype_level - Show the level of hype
# days_left - Days before the next trip
# hype_level_ru - Показать уровень хайпа до следующего события
# days_left_ru - Показать количество дней до следующего события

def days_left_en(bot, update):
  set_locale('en')
  days_left(bot, update)

def days_left_ru(bot, update):
  set_locale('ru')
  days_left(bot, update)

def days_left(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id=chat_id, text=DaysLeft(next_event()).response())

def hype_level_en(bot, update):
  chat_id = update.message.chat_id

  hypeometer = Hypeometer(hype_level(), En)
  bot.send_message(chat_id=chat_id, text=hypeometer.hype_level())

def hype_level_ru(bot, update):
  chat_id = update.message.chat_id

  hypeometer = Hypeometer(hype_level(), Ru)
  bot.send_message(chat_id=chat_id, text=hypeometer.hype_level())

def next_event():
  return datetime(2019, 10, 25, 7, 0)

def hype_level():
  # mapping = [5, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
  # countdown = Countdown(next_event(), Ru)
  # days_left = countdown.difference().days
  # return mapping[days_left]
  return 3

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
