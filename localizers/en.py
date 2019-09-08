from .base import Base

class En(Base):
  @classmethod
  def pick_number(singular, plural, value):
    if value == 1:
      return singular

    return plural

  @classmethod
  def days(value):
    return En.pick_number('day', 'days', value)

  @classmethod
  def hours(value):
    return En.pick_number('hour', 'hours', value)

  @classmethod
  def minutes(value):
    return En.pick_number('minute', 'minutes', value)

  @classmethod
  def seconds(value):
    return En.pick_number('second', 'seconds', value)

  @classmethod
  def hype():
    return 'hype'
