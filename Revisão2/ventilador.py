class Ventilador:
    def __init__(self):
        self.__marca = ""
        self.__modelo = ""
        self.__velocidade = 0
        self.__ligado = False

    def __str__(self):
        return f"Marca: {self.__marca}\nModelo: {self.__modelo}\nVelocidade atual: {self.__velocidade}\nLigado: {self.__ligado}"
    
    @property
    def marca(self):
        return self.__marca
    @property
    def modelo(self):
        return self.__modelo
    @property
    def velocidade(self):
        return self.__velocidade
    @property
    def ligado(self):
        return self.__ligado

    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    @ligado.setter
    def ligado(self, ON):
        if self.__ligado == True:
            self.__ligado = "ligado"
        elif self.__ligado == False:
            self.__ligado = "desligado"
        else:
            print("Operação inválida")
    @velocidade.setter
    def velocidade(self, operacao):
        if self.__ligado == True:
            if operacao == "subir":
                if (self.__velocidade + 1) > 3:
                    self.__velocidade = 3
                else:
                    self.__velocidade += 1
            elif operacao == "descer":
                if (self.__velocidade - 1) < 0:
                    self.__velocidade = 0
                else:
                    self.__velocidade -= 1
        else:
            print("O ventilador está desligado, não é possível alterar a velocidade")
    