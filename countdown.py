from datetime import datetime
from time_difference import TimeDifference
from localizers.en import En
from localizers.ru import Ru

class Countdown:
  def __init__(self, event_date, localizer = En):
    self.next_event = event_date
    self.localizer = localizer

  def message(self):
    diff = self.__difference()

    return (
      f'{diff.days} {self.localizer.days(diff.days)} '
      f'{diff.hours} {self.localizer.hours(diff.hours)} '
      f'{diff.minutes} {self.localizer.minutes(diff.minutes)} '
      f'{diff.seconds} {self.localizer.seconds(diff.seconds)}'
    )

  def __difference(self):
    return TimeDifference(self.__seconds_left())

  def __current_time(self):
    return datetime.utcnow()

  def __delta(self):
    return self.next_event - self.__current_time()

  def __seconds_left(self):
    return int(self.__delta().total_seconds())
