import os
from dotenv import load_dotenv
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import database
from locales.configs import set_locale

load_dotenv()
database.connect()

from models.event import Event
from responders.days_left import DaysLeft
from responders.hype_level import HypeLevel
from responders.event_responder import EventResponder

# List of available commands
# register - Register a new event. Example: /register <date:DD-MM-YYYY> <event_name:string>
# delete - Delete an existing event. Example: /delete <event_name:string>
# list - List of existing events
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

  def days_left_en(self, bot, update, args):
    set_locale('en')
    self.days_left(bot, update, args)

  def days_left_ru(self, bot, update, args):
    set_locale('ru')
    self.days_left(bot, update, args)

  def days_left(self, bot, update, args):
    chat_id = update.message.chat_id
    self.set_namespace(chat_id)

    bot.send_message(chat_id=chat_id, text=DaysLeft.response(args))

  def hype_level_en(self, bot, update, args):
    set_locale('en')
    self.hype_level(bot, update, args)

  def hype_level_ru(self, bot, update, args):
    set_locale('ru')
    self.hype_level(bot, update, args)

  def hype_level(self, bot, update, args):
    chat_id = update.message.chat_id
    self.set_namespace(chat_id)

    bot.send_message(chat_id=chat_id, text=HypeLevel.response(args))

  def register(self, bot, update, args):
    chat_id = update.message.chat_id
    self.set_namespace(chat_id)

    bot.send_message(chat_id=chat_id, text=EventResponder.register(args))

  def list(self, bot, update):
    chat_id = update.message.chat_id
    self.set_namespace(chat_id)

    bot.send_message(chat_id=chat_id, text=EventResponder.list())

  def delete(self, bot, update, args):
    chat_id = update.message.chat_id
    self.set_namespace(chat_id)

    bot.send_message(chat_id=chat_id, text=EventResponder.delete(args))

  def set_namespace(self, chat_id):
    Event.__namespace__ = chat_id

  def bind_commands(self):
    dp = self.updater.dispatcher
    dp.add_handler(CommandHandler('hype_level', self.hype_level_en, pass_args=True))
    dp.add_handler(CommandHandler('days_left', self.days_left_en, pass_args=True))
    dp.add_handler(CommandHandler('hype_level_ru', self.hype_level_ru, pass_args=True))
    dp.add_handler(CommandHandler('days_left_ru', self.days_left_ru, pass_args=True))
    dp.add_handler(CommandHandler('register', self.register, pass_args=True))
    dp.add_handler(CommandHandler('list', self.list))
    dp.add_handler(CommandHandler('delete', self.delete, pass_args=True))

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

# from datetime import datetime
# Event.register_or_update(name='Test', take_place_at=datetime(2019, 10, 26))
# Event.__namespace__ = 'default'
# event = Event.next()
# print(event.name)
