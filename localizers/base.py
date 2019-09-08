from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
  @abstractmethod
  def days(value):
    pass

  @abstractmethod
  def hours(value):
    pass

  @abstractmethod
  def minutes(value):
    pass

  @abstractmethod
  def seconds(value):
    pass
