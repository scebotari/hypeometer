from models.event import Event
from utils.countdown import Countdown

class DaysLeft:
  def __init__(self):
    self.next_event = Event.next()

  def formatter(func):
    def func_wrapper(self, value):
      measurment = func(self)
      localized = ngettext(
        f'%(value)d {measurment[0]}',
        f'%(value)d {measurment[1]}',
        value
      )

      return localized % { 'value': value }
  
    return func_wrapper

  @formatter
  def days(self):
    return ['day', 'days']

  @formatter
  def hours(self):
    return ['hour', 'hours']

  @formatter
  def minutes(self):
    return ['minute', 'minutes']

  @formatter
  def seconds(self):
    return ['second', 'seconds']

  def response(self):
    if self.next_event == None:
      return _('There are no upcoming events registered')

    diff = Countdown(self.next_event.take_place_at).difference()

    return (
      f'{self.days(diff.days)} {self.hours(diff.hours)} '
      f'{self.minutes(diff.minutes)} {self.seconds(diff.seconds)}'
    )
