import os
from dotenv import load_dotenv
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from datetime import datetime
import database
from locales.configs import set_locale

load_dotenv()
database.connect()

from responders.days_left import DaysLeft
from responders.hype_level import HypeLevel

# List of available commands
# hype_level - Show the level of hype
# days_left - Days before the next trip
# hype_level_ru - Показать уровень хайпа до следующего события
# days_left_ru - Показать количество дней до следующего события

class Bot:
  def __init__(self):
    self.mode = os.environ.get("MODE") or 'development'
    self.token = os.environ.get("TOKEN")
    self.updater = Updater(self.token)
    self.bind_commands()

  def days_left_en(self, bot, update):
    set_locale('en')
    self.days_left(bot, update)

  def days_left_ru(self, bot, update):
    set_locale('ru')
    self.days_left(bot, update)

  def days_left(self, bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=DaysLeft().response())

  def hype_level_en(self, bot, update):
    set_locale('en')
    self.hype_level(bot, update)

  def hype_level_ru(self, bot, update):
    set_locale('ru')
    self.hype_level(bot, update)    

  def hype_level(self, bot, update):
    chat_id = update.message.chat_id

    bot.send_message(chat_id=chat_id, text=HypeLevel().response())

  def bind_commands(self):
    dp = self.updater.dispatcher
    dp.add_handler(CommandHandler('hype_level', self.hype_level_en))
    dp.add_handler(CommandHandler('days_left', self.days_left_en))
    dp.add_handler(CommandHandler('hype_level_ru', self.hype_level_ru))
    dp.add_handler(CommandHandler('days_left_ru', self.days_left_ru))

  def run_production(self):
    port = int(os.environ.get("PORT", "8443"))
    app_name = os.environ.get("HEROKU_APP_NAME")

    self.updater.start_webhook(listen="0.0.0.0", port=port, url_path=self.token)
    self.updater.bot.set_webhook(
      "https://{}.herokuapp.com/{}".format(app_name, self.token)
    )

  def run_development(self):
    self.updater.start_polling()
    self.updater.idle()

  def run(self):
    if self.mode == 'prod':
      self.run_production()
    else:
      self.run_development()

def main():
  Bot().run()

if __name__ == '__main__':
  main()


# from models.event import Event
