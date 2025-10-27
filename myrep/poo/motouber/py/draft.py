class Pessoa:

    def __init__(self, nome:str, dinheiro:int):
        self.__nome: str = nome
        self.__dinheiro: int = dinheiro

    def __str__(self):
       return f"{self.__nome}:{self.__dinheiro}"
    
    def show(self):
        print(self)

    def getDinheiro(self):
        return self.__dinheiro

    def setDinheiroP(self, valor: int):
        self.__dinheiro -= valor
        if self.__dinheiro < valor:
            self.__dinheiro = 0

    def setDinheiroM(self, valor:int):
        self.__dinheiro += valor
    
class Moto:

    def __init__(self):
        self.__custo: int = 0
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None

    def __str__(self):
        return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"
    def show(self):
        print(self)

    def setDriver(self, motorista: Pessoa):
        self.__motorista = motorista

    def setPass(self, passageiro: Pessoa):
        self.__passageiro = passageiro

    def drive(self, valor:int):
        self.__custo += valor

    def leavePass(self):
        aux: Pessoa = self.__passageiro
        aux.setDinheiroP(self.__custo)
        self.__motorista.setDinheiroM(self.__custo)
        self.__passageiro = None
        if aux.getDinheiro() < self.__custo:
            print("fail: Passenger does not have enough money")
            
        print(f"{aux} left")
        self.__custo = 0
        

def main():
    pessoa = Pessoa("", 0)
    moto = Moto()

    while True:
        linha = input()
        args: list[str] = linha.split(" ")
        print("$" + linha)

        if args[0] == "end":
            break
        elif args[0] == "show":
            moto.show()
        elif args[0] == "setDriver":
            nome: str = args[1]
            dinheiro: int = int(args[2])
            motorista = Pessoa(nome, dinheiro)
            moto.setDriver(motorista)
        elif args[0] == "setPass":
            nome: str = args[1]
            dinheiro: int = int(args[2])
            passageiro = Pessoa(nome, dinheiro)
            moto.setPass(passageiro)
        elif args[0] == "drive":
            valor: int = int(args[1])
            moto.drive(valor)
        elif args[0] == "leavePass":
            moto.leavePass()
main()