class Show:
  def __init__(self, event, diff):
    self.event = event
    self.diff = diff

  def render(self):
    return (
      f'{self.header}\n'
      f'{self.days} {self.hours} {self.minutes} {self.seconds}'
    )

  @property
  def days(self):
    return self.formatted_value('day', 'days', self.diff.days)

  @property
  def hours(self):
    return self.formatted_value('hour', 'hours', self.diff.hours)

  @property
  def minutes(self):
    return self.formatted_value('minute', 'minutes', self.diff.minutes)

  @property
  def seconds(self):
    return self.formatted_value('second', 'seconds', self.diff.seconds)

  @property
  def header(self):
    return _('"%(name)s" will take place in:') % { 'name': self.event.name }

  def formatted_value(self, singular, plural, value):
    localized = ngettext(
      f'%(value)d {singular}',
      f'%(value)d {plural}',
      value
    )

    return localized % { 'value': value }
