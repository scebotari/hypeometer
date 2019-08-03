from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from countdown import Countdown
from datetime import datetime

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

def main():
  updater = Updater('915978703:AAEq14kYuPXOGEdk-yHNAe7dllrTQwUEHCo')
  dp = updater.dispatcher
  dp.add_handler(CommandHandler('hype_level', hype_level_en))
  dp.add_handler(CommandHandler('days_left', days_left_en))
  dp.add_handler(CommandHandler('hype_level_ru', hype_level_ru))
  dp.add_handler(CommandHandler('days_left_ru', days_left_ru))
  updater.start_polling()
  updater.idle()

if __name__ == '__main__':
  main()
