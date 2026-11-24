class Aluno:
  def __init__(self):
    self.__nome = ""
    self.__curso = ""
    self.__nota = 0.0

  @property
  def nome(self):
    return self.__nome
  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  @property
  def curso(self):
    return self.__curso
  @curso.setter
  def curso(self, curso):
    self.__curso = curso

  @property
  def nota(self):
    if (self.__nota > 10) or (self.__nota < 0):
      return self.__nota == 0
    else:
      return self.__nota
  @nota.setter
  def nota(self , nota):
    if (nota > 10) or (nota < 0):
      self.__nota = 0
    else:
      self.__nota = nota


a1 = Aluno()
a1.nome = "Maligno"
a1.curso = "A"
a1.nota = 7
print(f"Aluno {a1.nome} do curso {a1.curso} com a nota {a1.nota}")