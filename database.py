import os
from walrus import *

connection = None

def connect():
  global connection
  connection = Walrus.from_url(os.environ.get("REDIS_URL"))
