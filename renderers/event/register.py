class Register:
  def __init__(self, event):
    self.event = event

  def render(self):
    return (
      f'Event "{self.event.name}" was successfully registered for '
      f'{self.formatted_date}'
    )

  @property
  def formatted_date(self):
    return self.event.take_place_at.strftime("%d-%m-%Y")
