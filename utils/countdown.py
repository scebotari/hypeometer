from datetime import datetime
from .time_difference import TimeDifference

class Countdown:
  def __init__(self, date):
    self.date = date

  def difference(self):
    return TimeDifference(self.__seconds_left())

  def __current_time(self):
    return datetime.utcnow()

  def __delta(self):
    return self.date - self.__current_time()

  def __seconds_left(self):
    return int(self.__delta().total_seconds())
