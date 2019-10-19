from datetime import datetime

from models.event import Event

class EventResponder:
  @classmethod
  def parse_date(self, date_str):
    return datetime.strptime(date_str, '%d-%m-%Y')

  @classmethod
  def compile_name(self, name_args):
    return ' '.join(name_args)

  @classmethod
  def register(cls, args):
    if len(args) < 2:
      return ('Wrong number of arguments. Expected date and event name.')

    try:
      date = cls.parse_date(args[0])
    except ValueError:
      return (
        'Date format is invalid. Expected fortmat is "DD-MM-YYYY". '
        'Example: "29-10-2018".'
      )

    name = cls.compile_name(args[1:])

    event = Event.register_or_update(name=name, take_place_at=date)

    return (
      f'Event "{event.name}" was successfully registered for '
      f'{event.take_place_at.strftime("%d-%m-%Y")}'
    )
