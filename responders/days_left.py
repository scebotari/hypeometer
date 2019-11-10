from responders.base_responder import BaseResponder
from utils.countdown import Countdown
from utils.countfurther import Countfurther
from renderers.days_left.show import Show
from renderers.days_left.show_archived import ShowArchived

class DaysLeft(BaseResponder):
  @classmethod
  @BaseResponder.event_based
  def show(cls, event):
    if event.is_archived():
      return cls.show_archived(event)

    diff = Countdown(event.take_place_at).difference()

    return Show(event, diff).render()

  @classmethod
  def show_archived(cls, event):
    diff = Countfurther(event.take_place_at).difference()

    return ShowArchived(event, diff).render()
