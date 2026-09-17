
# Crie a classe produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto.

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return f"{self.nome} - Preço R$ {self.preco:.2f}"

p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)


print(p1.etiqueta())
print(p2.etiqueta())