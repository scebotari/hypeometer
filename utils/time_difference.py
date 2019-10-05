class TimeDifference:
  def __init__(self, delta):
    self.total_seconds = delta.seconds
    self.__seconds = None
    self.__minutes = None
    self.__hours = None
    self.days = delta.days

  @property
  def seconds(self):
    if self.__seconds is None:
      self.__seconds = self.calculate_seconds()

    return self.__seconds

  @property
  def minutes(self):
    if self.__minutes is None:
      self.__minutes = self.calculate_minutes()

    return self.__minutes

  @property
  def hours(self):
    if self.__hours is None:
      self.__hours = self.calculate_hours()

    return self.__hours

  def calculate_seconds(self):
    return self.total_seconds % 60

  def calculate_minutes(self):
    return self.total_seconds // 60 % 60

  def calculate_hours(self):
    return self.total_seconds // 3600

  def __str__(self):
    return 'TimeDifference(days={}, hours={}, mins={}, secs={})'.format(
      self.days, self.hours, self.minutes, self.seconds
    )
