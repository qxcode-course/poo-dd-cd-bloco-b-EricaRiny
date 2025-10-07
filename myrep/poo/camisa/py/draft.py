class Camisa:

    def __init__(self):
        self.__tamanho:str = ""

    def setTamanho(self, valor:str):
        if valor == "PP" or valor == "P" or valor == "M" or valor == "G" or valor == "GG" or valor == "XG":
            self.__tamanho   = valor
        else:
            print("tamanho invalido")


    def getTamanho(self):
        return self.__tamanho
        
camisa = Camisa()

while camisa.getTamanho() == "":
    print("digite seu tamanho de roupa")
    tamanho = input()
    camisa.setTamanho(tamanho)
print("parabens, voce comprou uma camisa temanho", camisa.getTamanho())
        