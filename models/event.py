from walrus import *
from datetime import datetime

from database import connection

class Event(Model):
  __database__ = connection
  __namespace__ = 'default'

  name = TextField(primary_key=True)
  registered_at = DateTimeField()
  take_place_at = DateTimeField()

  @classmethod
  def register(cls, **attrs):
    attrs['registered_at'] = datetime.utcnow()
    return cls.create(**attrs)    

  @classmethod
  def register_or_update(cls, **attrs):
    try:
      existing = cls.load(attrs['name'])
      existing.take_place_at = attrs['take_place_at']
      existing.save()
      return existing
    except KeyError:
      return cls.register(**attrs)

  @classmethod
  def next(cls):
    return next(Event.query(order_by=Event.take_place_at), None)

  @classmethod
  def all(cls):
    return cls.query(order_by=cls.take_place_at)