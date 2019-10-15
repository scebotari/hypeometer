from models.event import Event
from utils.hypeometer import Hypeometer

class HypeLevel:
  SCALE = 50

  def __init__(self):
    self._next_event = Event.next()
    self._percentage = None

  @property
  def next_event(self):
    return self._next_event

  @property
  def percentage(self):
    if self._percentage == None:
      self._percentage = Hypeometer(
        self.next_event.registered_at, self.next_event.take_place_at
      ).percentage

    return self._percentage

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
    if self.next_event == None:
      return _('There are no upcoming events registered')

    return (
      f'{self.title}:\n{self.scale}\n{self.padding}^ {self.percentage}%'
    )
