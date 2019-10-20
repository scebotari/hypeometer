from responders.base_responder import BaseResponder
from utils.hypeometer import Hypeometer

class HypeLevel(BaseResponder):
  SCALE = 50

  @classmethod
  def title(cls, name):
    return _('Hype level for "%(name)s"') % { 'name': name }

  @classmethod
  def scale(cls):
    return '0.........................................100'

  @classmethod
  def padding(cls, percentage):
    value = cls.SCALE * percentage // 100 - 1
    return ' ' * value

  @classmethod
  @BaseResponder.event_based
  def response(cls, event):
    percentage = Hypeometer(
      event.registered_at, event.take_place_at
    ).percentage

    return (
      f'{cls.title(event.name)}:\n{cls.scale()}\n'
      f'{cls.padding(percentage)}^ {percentage}%'
    )
