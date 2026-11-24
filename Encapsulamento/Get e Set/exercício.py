class Pessoa:
  def __init__(self, nome = "", idade = ""):
    self.__nome = nome
    self.__idade = idade

  def __str__(self):
    return f"Olá {self.__nome}, você tem {self.__idade}"

  def getNome(self):
    return self.__nome
  def setNome(self, nome):
    self.__nome = nome.upper()

  def getIdade(self):
    return self.__idade
  def setIdade(self, idade):
    self.__idade = idade.upper()

p1 = Pessoa()
p1.setNome("Marcelo")
p1.setIdade("18")
print(f"O seu nome é {p1.getNome()}")
print(f"A sua idade é {p1.getIdade()}")