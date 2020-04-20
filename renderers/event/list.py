from renderers.event.show import Show

class List:
  def __init__(self, upcoming, archived):
    self.upcoming = upcoming
    self.archived = archived

  def render(self):
    upcoming_response = self.render_upcoming()
    archived_response = self.render_archived()

    if not archived_response:
      return upcoming_response

    return f'{upcoming_response}\n\n{archived_response}'

  def render_upcoming(self):
    response_lines = []

    for event in self.upcoming:
      response_lines.append(Show(event).render_inline())

    if len(response_lines) == 0:
      return 'No upcoming events'

    response_lines.insert(0, 'Upcoming events:')
    return '\n'.join(response_lines)

  def render_archived(self):
    response_lines = []

    for event in self.archived:
      response_lines.append(Show(event).render_inline())

    if len(response_lines) == 0:
      return ''

    response_lines.insert(0, 'Archived events:')
    return '\n'.join(response_lines)
