class Celular:
    def __init__(self):
        self.__marca = ""
        self.__volume = 0

    @property
    def marca(self):
        return self.__marca
    @property
    def volume(self):
        return self.__volume

    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    @volume.setter
    def volume(self, n):
        if n < 0:
            if (self.__volume + n) < 0:
                self.__volume = 0
            else:
                self.__volume += n
        else:
            if (self.__volume + n) > 100:
                self.__volume = 100
            else:
                self.__volume += n

#Teste
c = Celular()
c.marca = "Samsung"
c.volume = 50
print(f"O volume atual é {c.volume}")
c.volume = 51
print(f"o volume atual é {c.volume}")