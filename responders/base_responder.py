from models.event import Event

class BaseResponder:
  @classmethod
  def parse_date(self, date_str):
    return datetime.strptime(date_str, '%d-%m-%Y')

  @classmethod
  def compile_name(self, name_args):
    return ' '.join(name_args)

  @classmethod
  def set_event(cls, name=None):
    if not name:
      return Event.next()

    return Event.load(name)

  def event_based(func):
    def func_wrapper(cls, args):
      name = cls.compile_name(args)

      try:
        event = cls.set_event(name)
      except KeyError:
        return _('Event "%(name)s" is not registered') % { 'name': name }

      if event == None:
        return _('There are no upcoming events registered')

      return func(cls, event)
  
    return func_wrapper
