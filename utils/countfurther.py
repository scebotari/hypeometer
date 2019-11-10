from datetime import datetime
from .countdown import Countdown

class Countfurther(Countdown):
  def _start_point(self):
    return self.date

  def _end_point(self):
    return max(datetime.utcnow(), self._start_point())
