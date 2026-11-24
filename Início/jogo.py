class Jogo:
  def __init__(self):
    self.categoria = ""
    self.nome = ""
    self.valor = 0.0
    self.armazenamento = 0.0
    self.avaliacao = ""
    self.dataLancamento = ""
  #Fim do construtor
  def aplicarDesconto(self, porcentagem):
    return self.valor - (self.valor * (porcentagem/100))

#Aqui estou fora da classe, imagine um arquivo separado!
#Instanciando o objeto

j1 = Jogo() #Sem parametros no construtor
j2 = Jogo() #Sem parametros no construtor

#Inserindo valores Jogo 1
j1.nome = "Gta VI"
j1.categoria = "Ação e Aventura"
j1.armazenamento = 250.0
j1.valor = 440.0
j1.dataLancamento = "19/11/2026"
j1.avaliacao = "N/A"

#Exibindo os valores
print(j1.nome, j1.valor)

#Aplicando desconto
print("Novo valor: ", j1.aplicarDesconto(25))