import unittest
from datetime import datetime, timedelta

from dotenv import load_dotenv
import database

from models.event import Event
from renderers.event.list import List

class TestList(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    load_dotenv('tests/.env')
    database.connect()
    Event.__database__ = database.connection
  
  def tearDown(self):
    Event.query_delete()

  # Tests

  def test_render(self):
    # Returns no events string, when there are no events
    responder = List([], [])
    self.assertEqual(responder.render(), 'No upcoming events')

    # Returns header and events, when there are upcoming events
    next_year = datetime.today().year + 1
    upcoming = [
      Event.create(
        name='Test event',
        take_place_at=datetime(next_year, 1, 1)
      )
    ]
    responder = List(upcoming, [])
    self.assertEqual(
      responder.render(),
      f'Upcoming events:\n01-01-{next_year} - "Test event"'
    )

    # Returns no upcoming events and archived events,
    # when there are no upcoming events, but there are archived
    archived = [
      Event.create(
        name='Test event',
        take_place_at=datetime(2020, 1, 1)
      )
    ]
    responder = List([], archived)
    self.assertEqual(
      responder.render(),
      'No upcoming events\n\nArchived events:\n01-01-2020 - "Test event"'
    )

    # Returns events lists
    responder = List(upcoming, archived)
    self.assertEqual(
      responder.render(),
      (
        f'Upcoming events:\n01-01-{next_year} - "Test event"'
        '\n\nArchived events:\n01-01-2020 - "Test event"'
      )
    )

  def test_render_upcoming(self):
    # Returns no events string, when there are no upcoming events
    responder = List([], [])
    self.assertEqual(responder.render_upcoming(), 'No upcoming events')

    # Returns header and events, when there are upcoming events
    next_year = datetime.today().year + 1
    upcoming = [
      Event.create(
        name='Test event',
        take_place_at=datetime(next_year, 1, 1)
      )
    ]
    responder = List(upcoming, [])
    self.assertEqual(
      responder.render_upcoming(),
      f'Upcoming events:\n01-01-{next_year} - "Test event"'
    )

  def test_render_archived(self):
    # Returns empty string, when there are no archived events
    responder = List([], [])
    self.assertEqual(responder.render_archived(), '')

    # Returns header and events, when there are archived events
    archived = [
      Event.create(
        name='Test event',
        take_place_at=datetime(2020, 1, 1)
      )
    ]
    responder = List([], archived)
    self.assertEqual(
      responder.render_archived(),
      'Archived events:\n01-01-2020 - "Test event"'
    )

if __name__ == '__main__':
  unittest.main()
