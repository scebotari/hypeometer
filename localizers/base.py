from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
  @classmethod
  @abstractmethod
  def days(cls, value):
    pass

  @classmethod
  @abstractmethod
  def hours(cls, value):
    pass

  @classmethod
  @abstractmethod
  def minutes(cls, value):
    pass

  @classmethod
  @abstractmethod
  def seconds(cls, value):
    pass
