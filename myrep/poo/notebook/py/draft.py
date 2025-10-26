class Bateria:

    def __init__(self, capacidade:int):
        self.__capacidade:int = capacidade
        self.__carga:int = capacidade
    
    def __str__(self):
        return f"({self.__carga}/{self.__capacidade})"
    
    def show(self):
        print(self)

    def getCarga(self):
        return self.__carga
    
    def getCapacidade(self):
        return self.__capacidade
    
    def setCarga(self, valor:int):
        
        if valor > self.__carga:
            valor = self.__carga
            self.__carga = 0
            print(f"usando por {valor} minutos, notebook descarregou")
        else:
            self.__carga -= valor

class Carregador:

    def __init(self, potencia:int):
        self.__potencia: int = potencia

    

class Notebook:

    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: None | Bateria = None
        self.__carregador: None | Carregador = None

    
    def ligar(self):
        if self.__ligado == False and bateria != None:
            self.__ligado = True

            print("notebook ligado")
        elif self.__ligado == False and self.__bateria == None:
            print("Nao foi possivel ligar")

        elif self.__ligado == True:
            print("Notebook ja esta ligado")


    def desligar(self):
        if self.__ligado == False:
            print("Notebook ja esta desligado")
        elif self.__ligado == True:
            print("notebook desligado")
            self.__ligado = False

    def mostrar(self):

        if self.__ligado == True:
            print(f"status: ligado, Bateria: {self.__bateria.__str__()}")
       
        elif self.__ligado == False and self.__bateria == None:
            print("status: desligado, Bateria: Nenhuma")

        elif self.__ligado == False:
            print(f"status: desligado, Bateria: {self.__bateria.__str__()}")


    def usar(self, tempo:int):
        if self.__ligado == False:
            print("ligue o notebook para usar")
        else:
            self.__bateria.setCarga(tempo)

    
    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria

    def removerBat(self):
        self.__bateria = None
        self.__ligado = False
        print("bateria removida")



notebook = Notebook()
notebook.mostrar()
notebook.usar(10)
bateria = Bateria(50)
bateria.show()
notebook.setBateria(bateria)
notebook.ligar()
notebook.usar(10)
notebook.mostrar()
bateria = notebook.removerBat()
notebook.mostrar()





