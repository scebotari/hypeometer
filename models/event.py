from walrus import *
from datetime import datetime

from database import connection

class Event(Model):
  __database__ = connection
  __namespace__ = 'default'

  name = TextField(primary_key=True)
  registered_at = DateTimeField()
  take_place_at = DateTimeField(index=True)

  def is_upcoming(self):
    return self.take_place_at >= datetime.utcnow()

  def is_archived(self):
    return not self.is_upcoming()

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
    return next(cls.upcoming(), None)

  @classmethod
  def all(cls):
    return cls.query(order_by=cls.take_place_at)

  @classmethod
  def upcoming(cls):
    return cls.query(
      cls.take_place_at >= datetime.utcnow(),
      order_by=cls.take_place_at
    )

  @classmethod
  def archived(cls):
    return cls.query(
      cls.take_place_at < datetime.utcnow(),
      order_by=cls.take_place_at.desc()
    )
