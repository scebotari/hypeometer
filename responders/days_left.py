from utils.countdown import Countdown

class DaysLeft:
  def __init__(self, next_event_date):
    self.next_event_date = next_event_date

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
    diff = Countdown(self.next_event_date).difference()

    return (
      f'{self.days(diff.days)} {self.hours(diff.hours)} '
      f'{self.minutes(diff.minutes)} {self.seconds(diff.seconds)}'
    )
