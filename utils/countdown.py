from datetime import datetime
from .time_difference import TimeDifference

class Countdown:
  def __init__(self, date):
    self.date = date

  def difference(self):
    return TimeDifference(self.__delta())

  def _start_point(self):
    return min(datetime.utcnow(), self._end_point())

  def _end_point(self):
    return self.date

  def __delta(self):
    return self._end_point() - self._start_point()
