class Aluno:
  def __init__(self, nome = "", curso = "", nfaltas = 0):
    self.nome = nome
    self.curso = curso
    self.nfaltas = nfaltas

  def __str__(self):
    return f"O aluno(a) {self.nome} do curso {self.curso} e tem {self.nfaltas} números de faltas."


class Turma:
  def __init__(self, alunos = []):
    self.alunos = alunos

  def adicionar_aluno(self, aluno=Aluno()):
    self.alunos.append(aluno)

  def __str__(self):
    quantidade = len(self.alunos)
    return f"A turma possui {quantidade} alunos cadastrados."

t1 = Turma()
resp = "s"
while resp == "s":
  a = Aluno()
  a.nome = input("Digite o nome do aluno: ")
  a.curso = input("Digite o nome do curso: ")
  a.nfaltas = input("Digite o número de faltas: ")
  t1.adicionar_aluno(a)
  print("")
  resp = input("Deseja cadastrar outro aluno (s/n)? ").lower()

print("Turma completa. Imprimindo itens.")
print(t1)
for i in t1.alunos:
  print(i)