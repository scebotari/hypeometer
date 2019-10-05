from datetime import datetime
from .time_difference import TimeDifference

class Countdown:
  def __init__(self, date):
    self.date = date

  def difference(self):
    return TimeDifference(self.__delta())

  def __current_time(self):
    return datetime.utcnow()

  def __delta(self):
    return self.date - self.__current_time()
