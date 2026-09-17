# Crie a classe Churrasco, onde seka possivel informar
# quantas pessoas vão participar e mostre quanto de carne
# deve ser comprado, o custo total do churrasco e o
# preço por pessoa...


# CONSIDERE:
# Consumo padrão: 400g por pessoa
# Preço: R$82,40/Kg

class Churrasco:

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
        self.preco = 82.40
        self.KG = self.calcularKG(self.quant)
        self.Valor = self.calcularVALOR()


    def calcularKG(self, q):
        totalKG = q * 0.400
        return totalKG

    def calcularVALOR(self):
        totalValor = self.KG * self.preco
        return totalValor

    def apresentar(self):
        return f"Para {self.quant} pessoas, é necessário comprar {self.KG:.3f}Kg de carne. O valor total é R$ {self.Valor:.2f}"


c1 = Churrasco("Churras do Amigos", 100)
print(c1.apresentar())
