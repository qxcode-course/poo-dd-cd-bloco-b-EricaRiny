class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.__nome:str = nome
        self.__idade:str = idade

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def __str__(self):
        return f"{self.__nome}:{self.__idade}"
    
    def show(self):
        print(self)
    
    
class Motoca:

    def __init__(self, potencia:int):
        self.__potencia:int = potencia
        self.__tempo:int = 0
        self.__pessoa: Pessoa | None = None

    def __str__(self):
        if self.__pessoa == None:
            return f"power:{self.__potencia}, time:{self.__tempo}, person:(empty)"
        else:
            return f"power:{self.__potencia}, time:{self.__tempo}, person:({self.__pessoa})"
    def show(self):
        print(self)

    def subir(self, nome:str, idade:int):
        if self.__pessoa != None:
            print("fail: busy motorcycle")
        else:
            self.__pessoa = Pessoa(nome, idade)  

    def sair(self):

        if self.__pessoa != None:
            aux = self.__pessoa
            self.__pessoa = None
            print(aux)
        else:
            print("fail: empty motorcycle")

    def comprar(self, valor:int):
        self.__tempo += valor

    def dirigir(self, valor:int):
        if self.__tempo == 0:
            print("fail: buy time first")
        elif self.__pessoa == None:
            print("fail: empty motorcycle")
        elif self.__tempo < valor:
            valor = self.__tempo
            self.__tempo = 0
            print(f"fail: time finished after {valor} minutes")
        elif self.__pessoa.getIdade() > 10:
            print("fail: too old to drive")
        else:
            self.__tempo -= valor
    
    def buzina(self):
        buzina = "P" + ("e" * self.__potencia) + "m"
        print(buzina)

def main():

    pessoa = Pessoa("", 0)
    motoca = Motoca(1)

    while True:
        linha = input()
        args: list[str] = linha.split(" ")

        print("$" + linha)

        if args[0] == "end":
            break
        elif args[0] == "show":
            motoca.show() 
        elif args[0] == "enter":
            nome:str = args[1]
            idade:int = int(args[2])
            motoca.subir(nome, idade)
        elif args[0] == "init":
            potencia:int = int(args[1])
            motoca = Motoca(potencia)
        elif args[0] == "leave":
            motoca.sair()
        elif args[0] == "buy":
            valor:int = int(args[1])
            motoca.comprar(valor)
        elif args[0] == "drive":
            valor:int = int(args[1])
            motoca.dirigir(valor)
        elif args[0] == "honk":
            motoca.buzina()

main()
    