class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.__calibre: float = calibre
        self.__dureza : float = dureza
        self.__tamanho: int = tamanho


    def getCalibre(self):
        return self.__calibre
    
    def getDureza(self):
        return self.__dureza
    
    def getTamanho(self):
        return self.__tamanho
    
    def __str__(self):
        return f"[{self.__calibre}:{self.__dureza}:{self.__tamanho}]"
    
    def show(self):
        print(self)

    def gastoPorFolha(self):
        if self.__dureza == "HB":
            self.__tamanho -= 1
        elif self.__dureza == "2B":
            self.__tamanho -= 2
        elif self.__dureza == "4B":
            self.__tamanho -= 4
        elif self.__dureza == "6B":
            self.__tamanho -= 6
        if self.__tamanho < 10:
            self.__tamanho = 10
            print("fail: folha incompleta")
    
class Lapiseira:
    
    def __init__(self, calibre:int):
        self.__calibre: str = calibre
        self.__ponta: Grafite | None = None

    def __str__(self):
        if self.__ponta == None:
            return f"calibre: {self.__calibre}, grafite: null"
        else:
            return f"calibre: {self.__calibre}, grafite: {self.__ponta}"
    
    def show(self):
        print(self)
        
    def temGrafite(self):
        if self.__ponta != None:
            return True
        else:
            return False
        
    def inserir(self, grafite: Grafite):
        if self.temGrafite():
            print("fail: ja existe grafite")
            
        elif self.__calibre != grafite.getCalibre():
            print("fail: calibre incompativel") 
            
        else:
            self.__ponta = grafite

    def remover(self):
        self.__ponta = None
    
    def escrever(self):
        if self.temGrafite() == False:
            print("fail: nao existe grafite")
        elif self.__ponta.getTamanho() > 10:
            self.__ponta.gastoPorFolha()
        elif self.__ponta.getTamanho() <= 10:
            print("fail: tamanho insuficiente")
            

            
def main():
    lapiseira = Lapiseira(0)
    grafite = Grafite(0, "", 0)

    while True:
        linha = input()
        args: list[str] = linha.split(" ")
        print("$" + linha)

        if args[0] == "end":
            break
        elif args[0] == "init":
            calibre: float = float(args[1])
            lapiseira = Lapiseira(calibre)
        elif args[0] == "show":
            lapiseira.show()
        elif args[0] == "insert":
            calibre: float = float(args[1])
            dureza: str = args[2]
            tamanho: int = int(args[3])
            grafite = Grafite(calibre, dureza, tamanho)
            lapiseira.inserir(grafite)
        elif args[0] == "remove":
            lapiseira.remover()
        elif args[0] == "write":
            lapiseira.escrever()
main()