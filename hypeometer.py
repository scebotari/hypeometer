import random

from localizers.en import En
from localizers.ru import Ru

class Hypeometer:
  def __init__(self, hypelevel=5, localizer=En):
    self.level = hypelevel
    self.localizer = localizer

  def hype_level(self):
    level_func = {
      1: self.level_1,
      2: self.level_2,
      3: self.level_3,
      4: self.level_4,
      5: self.level_5,
    }.get(self.level, 1)

    return level_func()

  def level_1(self):
    return self.localizer.hype().capitalize()

  def level_2(self):
    hype = self.localizer.hype().capitalize()
    return '{}!'.format(hype)

  def level_3(self):
    hype = self.localizer.hype().capitalize()
    return '{}!!!'.format(hype)

  def level_4(self):
    hype = self.localizer.hype().upper()
    return '{}!!!!!'.format(hype)

  def level_5(self):
    hype = self.localizer.hype().upper()

    exclamations = []
    for x in range(10):
      exclamations.append(['!', '!', '!', '1'][random.randint(0, 3)])

    return '{}{}'.format(hype, ''.join(exclamations))

  @property
  def level(self):
    return self._level

  @level.setter
  def level(self, value):
    if value < 1:
      self._level = 1
    elif value > 5:
      self._level = 5
    else:
      self._level = value
