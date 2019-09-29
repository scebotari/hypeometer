from .base import Base

class En(Base):
  @classmethod
  def pick_number(cls, singular, plural, value):
    if value == 1:
      return singular

    return plural

  @classmethod
  def days(cls, value):
    return cls.pick_number('day', 'days', value)

  @classmethod
  def hours(cls, value):
    return cls.pick_number('hour', 'hours', value)

  @classmethod
  def minutes(cls, value):
    return cls.pick_number('minute', 'minutes', value)

  @classmethod
  def seconds(cls, value):
    return cls.pick_number('second', 'seconds', value)

  @classmethod
  def hype(cls):
    return 'hype'
