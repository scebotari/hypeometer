from responders.base_responder import BaseResponder
from utils.hypeometer import Hypeometer
from renderers.hype_level.show import Show

class HypeLevel(BaseResponder):
  @classmethod
  @BaseResponder.event_based
  def response(cls, event):
    percentage = Hypeometer(
      event.registered_at, event.take_place_at
    ).percentage

    return Show(event, percentage).render()
