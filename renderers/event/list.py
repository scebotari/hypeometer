from renderers.event.show import Show

class List:
  def __init__(self, upcoming, archived):
    self.upcoming = upcoming
    self.archived = archived

  def render(self):
    return f'{self.render_upcoming()}\n\n{self.render_archived()}'

  def render_upcoming(self):
    response_lines = ['Upcoming events:']

    for event in self.upcoming:
      response_lines.append(Show(event).render_inline())

    return '\n'.join(response_lines)

  def render_archived(self):
    response_lines = ['Archived events:']

    for event in self.archived:
      response_lines.append(Show(event).render_inline())

    return '\n'.join(response_lines)
