class TimeDifference:
  def __init__(self, total_seconds):
    self.total_seconds = total_seconds
    self._seconds = None
    self._minutes = None
    self._hours = None
    self._days = None

  @property
  def seconds(self):
    if self._seconds is None:
      self._seconds = self.calculate_seconds()

    return self._seconds

  @property
  def minutes(self):
    if self._minutes is None:
      self._minutes = self.calculate_minutes()

    return self._minutes

  @property
  def hours(self):
    if self._hours is None:
      self._hours = self.calculate_hours()

    return self._hours

  @property
  def days(self):
    if self._days is None:
      self._days = self.calculate_days()

    return self._days

  def calculate_seconds(self):
    return self.total_seconds % 60

  def calculate_minutes(self):
    return self.total_seconds // 60 % 60

  def calculate_hours(self):
    return self.total_seconds // 3600 % 24

  def calculate_days(self):
    return self.total_seconds // 86400

  def __str__(self):
    return 'TimeDifference(days={}, hours={}, mins={}, secs={})'.format(
      self.days, self.hours, self.minutes, self.seconds
    )
