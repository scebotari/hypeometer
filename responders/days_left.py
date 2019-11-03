from responders.base_responder import BaseResponder
from utils.countdown import Countdown
from renderers.days_left.show import Show

class DaysLeft(BaseResponder):
  @classmethod
  @BaseResponder.event_based
  def show(cls, event):
    diff = Countdown(event.take_place_at).difference()

    return Show(event, diff).render()
