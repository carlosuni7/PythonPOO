from traceback import print_tb

# Crie a Classe Funcionario, onde podemos cadastrar nome, setor, cargo. Crie também um método que permita ao funcionário se apresentar.

class Funcionario:

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = "Curso em Video"

    def apresentacao(self):
        return f"Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}"

c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())
c2 = Funcionario("Carlos Gonçalves", "TI", "Programador")
print(c2.apresentacao())
