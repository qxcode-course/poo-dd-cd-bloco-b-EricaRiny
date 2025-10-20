class Roupa:

    def __init__(self):
        self.__tamanho: str = ""
    
    def setTamanho(self, valor: str):
        if valor == "PP" or valor == "P" or valor == "M" or valor == "G" or valor == "GG" or valor == "XG":
            self.__tamanho = valor
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

    def __str__(self):
        return(f"size: ({self.__tamanho})")

    def show(self):
        print(self)
        
def main():
    roupa = Roupa()

    while True:
        linha = str(input())
        arg: list[str] = linha.split(" ")

        print("$" + linha)

        if arg[0] == "end":
            break
        elif arg[0] == "show":
            roupa.show()
        elif arg[0] == "size":
            valor:str = arg[1]
            roupa.setTamanho(valor)

main()