class Show:
  SCALE = 50

  def __init__(self, event, percentage):
    self.event = event
    self.percentage = percentage

  def render(self):
    return f'{self.title}:\n{self.scale}\n{self.pointer}'

  @property
  def pointer(self):
    return f'{self.padding}^ {self.percentage}%'
  
  @property
  def title(self):
    return _('Hype level for "%(name)s"') % { 'name': self.event.name }

  @property
  def scale(self):
    return '0.........................................100'

  @property
  def padding(self):
    value = self.SCALE * self.percentage // 100 - 1
    return ' ' * value
