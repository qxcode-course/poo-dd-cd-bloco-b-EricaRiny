class Chinela:
    
    def __init__(self):
       self.__tamanho:int = 0

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, valor:int):
        if valor < 20 or valor > 50:
            print("tamanho errado")
        elif valor % 2 != 0:
            print("tamanho errado")
        else:
            self.__tamanho = valor

chinela = Chinela()

while chinela.getTamanho() == 0:
    tamanho = int(input())
    chinela.setTamanho(tamanho)

print("Parabens, voce comprou uma chinela tamanho", chinela.getTamanho())


