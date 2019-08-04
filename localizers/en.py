from .base import Base

class En(Base):
  @staticmethod
  def pick_number(singular, plural, value):
    if value == 1:
      return singular

    return plural

  @staticmethod
  def days(value):
    return En.pick_number('day', 'days', value)

  @staticmethod
  def hours(value):
    return En.pick_number('hour', 'hours', value)

  @staticmethod
  def minutes(value):
    return En.pick_number('minute', 'minutes', value)

  @staticmethod
  def seconds(value):
    return En.pick_number('second', 'seconds', value)

  @staticmethod
  def hype():
    return 'hype'
