from datetime import datetime

from utils.hypeometer import Hypeometer

class HypeLevel:
  SCALE = 50

  def __init__(self, next_event_date):
    self.percentage = Hypeometer(
      datetime(2019, 9, 15, 7, 0), next_event_date
    ).percentage

  @property
  def title(self):
    return _('Hype level')

  @property
  def scale(self):
    return '0.........................................100'

  @property
  def padding(self):
    value = self.SCALE * self.percentage // 100 - 1
    return ' ' * value

  def response(self):
    return (
      f'{self.title}:\n{self.scale}\n{self.padding}^ {self.percentage}%'
    )
