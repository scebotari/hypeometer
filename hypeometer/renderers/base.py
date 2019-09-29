from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
  @classmethod
  @abstractmethod
  def render(cls, str):
    pass 
