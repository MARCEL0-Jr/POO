class Caneta:
  def __init__(self, cor = "", marca = ""):
    self.__cor = cor
    self.__marca = marca

  @property
  def cor(self):
    return self.__cor

  @cor.setter
  def cor(self, cor):
    self.__cor = cor

  @property
  def marca(self):
    return self.__marca

  @cor.seter
  def marca(self, marca):
    self.__marca = marca

c1 = Caneta()