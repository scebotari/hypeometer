from walrus import *

from database import connection

class Event(Model):
  __database__ = connection

  name = TextField()
  registered_at = DateTimeField()
  take_place_at = DateTimeField(index=True)

  @classmethod
  def next(cls):
    return next(Event.query(order_by=Event.take_place_at), None)

# Event.next().delete()
# from datetime import datetime
# Event.create(name='ESL', registered_at=datetime(2019, 10, 1), take_place_at=datetime(2019, 10, 25))
# for event in Event.all():
#   print(event.name, event.registered_at, event.take_place_at)
