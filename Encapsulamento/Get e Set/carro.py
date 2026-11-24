class Carro:
  def __init__(self, cor = "", marca = ""):
    self.__cor = cor #Atributo Privado
    self.__marca = marca #Atributo Privado

  def __str__(self):
    return f"Carro de marca {self.marca} e cor {self.cor}"

  #Métodos acessores
  def getCor(self):
    return self.__cor
  def setCor(self, cor):
    self.__cor = cor.upper()

  def getMarca(self):
    return self.__marca
  def setMarca(self, marca):
    self.__marca = marca.upper()

#Instanciando
c1 = Carro()
c1.setCor("Preto")
c1.setMarca("Gol")
print(f"A cor do carro: {c1.getCor()}")
print(f"A marca do carro: {c1.getMarca()}")