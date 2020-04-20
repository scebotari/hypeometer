import unittest
from datetime import datetime, timedelta

from dotenv import load_dotenv
import database
from models.event import Event

class TestEvent(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    load_dotenv('tests/.env')
    database.connect()
    Event.__database__ = database.connection
  
  def tearDown(self):
    Event.query_delete()

  def setUp(self):
    self.event = Event(**self.default_attrs())

  # Helper methods

  @staticmethod
  def default_attrs():
    return {
      'name': 'Test event',
      'take_place_at': (datetime.utcnow() + timedelta(days=10))
    }

  # Tests

  def test_is_upcoming(self):
    self.assertTrue(self.event.is_upcoming())

  def test_is_not_upcoming(self):
    self.event.take_place_at = datetime.utcnow() - timedelta(days=10)
    self.assertFalse(self.event.is_upcoming())
  
  def test_is_archived(self):
    self.event.take_place_at = datetime.utcnow() - timedelta(days=10)
    self.assertTrue(self.event.is_archived())

  def test_is_not_archived(self):
    self.assertFalse(self.event.is_archived())

  def test_register(self):
    Event.register(**self.default_attrs())

    self.assertEqual(Event.count(), 1)

    created_event = next(Event.query())
    self.assertIsInstance(created_event.registered_at, datetime)
    self.assertEqual(created_event.name, 'Test event')

  def test_register_or_update(self):
    # Creates an event, when there's no event with such name in DB
    Event.register_or_update(**self.default_attrs())
    self.assertEqual(Event.count(), 1)

    created_event = next(Event.query())
    self.assertIsInstance(created_event.registered_at, datetime)
    self.assertEqual(created_event.name, 'Test event')

    # Does not create a new event, if one with current name exists in DB
    Event.register_or_update(**self.default_attrs())
    self.assertEqual(Event.count(), 1)

  def test_next(self):
    # Returns None, when there are no events in the DB
    self.assertIsNone(Event.next())

    # Returns next event, if there are upcoming events
    Event.create(
      name = 'next',
      take_place_at = datetime.utcnow() + timedelta(days=1)
    )
    Event.create(
      name = 'last',
      take_place_at = datetime.utcnow() + timedelta(days=10)
    )
    next_event = Event.next()
    self.assertEqual(next_event.name, 'next')
  
  def test_all(self):
    # Returns no events, if DB is blank
    self.assertEqual(
      [],
      list(event.name for event in Event.all())
    )

    # Returns all events from DB
    Event.create(
      name = 'archived',
      take_place_at = datetime.utcnow() - timedelta(days=1)
    )
    Event.create(
      name = 'upcoming',
      take_place_at = datetime.utcnow() + timedelta(days=10)
    )

    self.assertEqual(
      ['archived', 'upcoming'],
      list(event.name for event in Event.all())
    )
  
  def test_upcoming(self):
    # Returns no events, if DB is blank
    self.assertEqual(
      [],
      list(event.name for event in Event.upcoming())
    )

    # Returns no events, if there are only archived events
    Event.create(
      name = 'archived',
      take_place_at = datetime.utcnow() - timedelta(days=1)
    )
    self.assertEqual(
      [],
      list(event.name for event in Event.upcoming())
    )

    # Returns upcoming events
    Event.create(
      name = 'upcoming',
      take_place_at = datetime.utcnow() + timedelta(days=10)
    )
    self.assertEqual(
      ['upcoming'],
      list(event.name for event in Event.upcoming())
    )
  
  def test_arhived(self):
    # Returns no events, if DB is blank
    self.assertEqual(
      [],
      list(event.name for event in Event.archived())
    )

    # Returns no events, if there are only upcoming events
    Event.create(
      name = 'upcoming',
      take_place_at = datetime.utcnow() + timedelta(days=10)
    )
    self.assertEqual(
      [],
      list(event.name for event in Event.archived())
    )

    # Returns archived events
    Event.create(
      name = 'archived',
      take_place_at = datetime.utcnow() - timedelta(days=1)
    )
    self.assertEqual(
      ['archived'],
      list(event.name for event in Event.archived())
    )

if __name__ == '__main__':
  unittest.main()
