from .base import Base

class Ru(Base):
  @classmethod
  def pick_number(cls, singular, plural1, plural2, value):
    if value > 9 and value < 21:
      return plural2
    if value % 10 == 1:
      return singular
    elif (value % 10) in (2, 3, 4):
      return plural1

    return plural2

  @classmethod
  def days(cls, value):
    return cls.pick_number('день', 'дня', 'дней', value)

  @classmethod
  def hours(cls, value):
    return cls.pick_number('час', 'часа', 'часов', value)

  @classmethod
  def minutes(cls, value):
    return cls.pick_number('минута', 'минуты', 'минут', value)

  @classmethod
  def seconds(cls, value):
    return cls.pick_number('секунда', 'секунды', 'секунд', value)

  @classmethod
  def hype(cls):
    return 'Хайп'
