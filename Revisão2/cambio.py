class Cambio:
    def __init__(self):
        self.__marca = ""
        self.__modelo = ""
        self.__ano = 0
        self.__marcha = 0

    def __str__(self):
        return f"Marca: {self.__marca}\nModelo: {self.__modelo}\nAno: {self.__ano}\nMarcha atual: {self.__marcha}"
    
    @property
    def marca(self):
        return self.__marca
    @property
    def modelo(self):
        return self.__modelo
    @property
    def ano (self):
        return self.__ano
    @property
    def marcha(self):
        return self.__marcha

    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    @marcha.setter
    def marcha(self, operacao):
        if operacao == "subir":
            if (self.__marcha + 1) > 6:
                self.__marcha = 0
            else:
                self.__marcha += 1 
        elif operacao == "descer":
            if (self.__marcha - 1) < 0:
                self.__marcha = 0
                print("Não é possível descer mais marchas")
            else:
                self.__marcha -= 1
        else:
            print("Operação inválida")

#Teste
c = Cambio()
c.marca = "Golf"
c.modelo = "GTI"
c.ano = 2020
print(c.marcha)
c.marcha = "subir"
print(c.marcha)
c.marcha = "subir"
print(c.marcha)
c.marcha = "descer"
print(c)