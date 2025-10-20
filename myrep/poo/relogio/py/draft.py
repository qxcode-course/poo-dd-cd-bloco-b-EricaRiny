class Relogio:
    def __init__(self, hora:int, minuto:int, segundo:int):
        self.__hora:int = hora
        self.__minuto:int = minuto
        self.__segundo:int = segundo
        
        if self.__hora > 23:
            print("fail: hora invalida")
            self.__hora = 0
        if self.__minuto > 59:
            print("fail: minuto invalido")
            self.__minuto = 0
        if self.__segundo > 59:
            print("fail: segundo invalido")
            self.__segundo = 0

    def getHora(self):
        return self.__hora
    def getMin(self):
        return self.__minuto
    def getSeg(self):
        return self.__segundo
    
    def __str__(self):
        return f"{self.__hora:02}:{self.__minuto:02}:{self.__segundo:02}"
    
    def show(self):
        print(self)

    def setHora(self, valor:int):
        if valor > 23 or valor < 0:
            print("fail: hora invalida")
        else:
            self.__hora = valor

    def setMin(self,valor:int):
        if valor > 59 or valor < 0:
            print("fail: minuto invalido")
        else:
            self.__minuto = valor

    def setSeg(self, valor:int):
        if valor > 59 or valor < 0:
            print("fail: segundo invalido")
        else:
            self.__segundo = valor
    
    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo > 59:
            self.__segundo = 0
            self.__minuto += 1
        if self.__minuto > 59:
            self.__minuto = 0
            self.__hora += 1
        if self.__hora > 23:
            self.__hora = 0

       
            


def main():

    relogio = Relogio(0, 0, 0)
    
    while True:
        linha = input()
        arg: list[int] = linha.split(" ")
        print("$" + linha)
        if arg[0] == "end":
            break
        elif arg[0] == "init":
            valor1:int = int(arg[1])
            valor2:int = int(arg[2])
            valor3:int = int(arg[3])
            relogio.__init__(valor1, valor2, valor3)
        elif arg[0] == "show":
            relogio.show()
        elif arg[0] == "set":
            valor1:int = int(arg[1])
            valor2:int = int(arg[2])
            valor3:int = int(arg[3])
            relogio.setHora(valor1)
            relogio.setMin(valor2)
            relogio.setSeg(valor3)
        elif arg[0] == "next":
            relogio.nextSecond()
        

main()