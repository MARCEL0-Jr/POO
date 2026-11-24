class Celular:
  def __init__(self):
    self.__marca = ""
    self.__volume = 0

  @property
  def volume(self):
    return self.__volume
  @property
  def marca(self):
    return self.__marca

  @volume.setter
  def volume(self, n):
    if n < 0:
      if (self.__volume + n) < 0:
        self.__volume = 0
      else:
        self.__volume = self.__volume + n
    else:
      if (self.__volume + n) > 100:
        self.__volume = 100
      else:
        self.__volume = self.__volume + n
  @marca.setter
  def marca(self, m):
    self.__marca = m

c = Celular()
c.marca = "Samsung"
c.volume = 50
print(f"valor inserido foi {c.volume}")
c.volume = -51
print(f"valor inserido foi {c.volume}")