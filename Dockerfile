FROM python:3.7

RUN pip install python-telegram-bot python-dotenv

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD python /app/hype_bot.py
