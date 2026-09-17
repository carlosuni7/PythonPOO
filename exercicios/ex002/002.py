# Tarefas nesse exercicio
# --- Melhorando nossas Classes
"""
-- 1. Como melhorar a classe da aula anterior?
-- 2. Como documentar uma classe?
-- 3. Como descobrir a classe de um objeto?
-- 4. Como obter o estado de um objeto?4
"""

# Declaração de Classe
class Gafanhoto:

# Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
# Para criar uma nova pessoa, use
# variavel = Gafanhoto(nome, idade)

    def __init__(self, nome = "vazio", idade = 0): # Método Construtor
        # atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): # Todo objeto possui metodo str, ele mostra o endereço da memória
        # aqui mostro os dados de uma maneira amigavel
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; Idade = {self.idade}"

# Declaração de Objetos
g1 = Gafanhoto("Maria", 20) # atribuindo valor ao atributo da classe
g1.aniversario()
print(g1)
print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Dunder Method
print(g1.__class__) # Dunder Attribute
# print(g1.__doc__) # Dunder Attribute
