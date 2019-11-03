class Show:
  def __init__(self, event):
    self.event = event

  def render_inline(self):
    return f'{self.formatted_date} - "{self.event.name}"'

  @property
  def formatted_date(self):
    return self.event.take_place_at.strftime("%d-%m-%Y")
