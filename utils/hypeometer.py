from datetime import datetime

class Hypeometer:
  def __init__(self, from_date, to_date):
    self.from_date = from_date
    self.to_date = to_date

  @property
  def percentage(self):
    return self.passed * 100 // (self.to_date - self.from_date)

  @property
  def passed(self):
    return self.__current_time() - self.from_date

  def __current_time(self):
    return datetime.utcnow()
