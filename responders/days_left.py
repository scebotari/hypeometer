from responders.base_responder import BaseResponder
from utils.countdown import Countdown

class DaysLeft(BaseResponder):
  def formatter(func):
    def func_wrapper(cls, value):
      measurment = func(cls)
      localized = ngettext(
        f'%(value)d {measurment[0]}',
        f'%(value)d {measurment[1]}',
        value
      )

      return localized % { 'value': value }
  
    return func_wrapper

  @classmethod
  @formatter
  def days(cls):
    return ['day', 'days']

  @classmethod
  @formatter
  def hours(cls):
    return ['hour', 'hours']

  @classmethod
  @formatter
  def minutes(cls):
    return ['minute', 'minutes']

  @classmethod
  @formatter
  def seconds(cls):
    return ['second', 'seconds']

  @classmethod
  def header(cls, name):
    return _('"%(name)s" will take place in:') % { 'name': name }

  @classmethod
  @BaseResponder.event_based
  def response(cls, event):
    diff = Countdown(event.take_place_at).difference()

    return (
      f'{cls.header(event.name)}\n'
      f'{cls.days(diff.days)} {cls.hours(diff.hours)} '
      f'{cls.minutes(diff.minutes)} {cls.seconds(diff.seconds)}'
    )
