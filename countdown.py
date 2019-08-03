from datetime import datetime
from time_difference import TimeDifference
from localizers.en import En
from localizers.ru import Ru

class Countdown:
  def __init__(self, event_date, locale = 'en'):
    self.next_event = event_date
    self._delta_cache = None
    self.locale = locale
    self._localizer = None

  def message(self):
    diff = self.difference()

    return '{} {} {} {} {} {} {} {}'.format(
      diff.days, self.localizer.days(diff.days),
      diff.hours, self.localizer.hours(diff.hours),
      diff.minutes, self.localizer.minutes(diff.minutes),
      diff.seconds, self.localizer.seconds(diff.seconds)
    )

  def difference(self):
    return TimeDifference(self.seconds_left())

  def current_time(self):
    return datetime.now()

  def delta(self):
    return self.next_event - self.current_time()

  def seconds_left(self):
    return int(self.delta().total_seconds())

  @property
  def localizer(self):
    if self._localizer is None:
      self._localizer = {
        'ru': Ru,
        'en': En
      }.get(self.locale, 'en')

    return self._localizer

# countdown = Countdown(datetime(2019, 8, 13, 7, 0), 'en')
# countdown_ru = Countdown(datetime(2019, 8, 13, 7, 0), 'ru')
# print(countdown.message())
# print(countdown_ru.message())
