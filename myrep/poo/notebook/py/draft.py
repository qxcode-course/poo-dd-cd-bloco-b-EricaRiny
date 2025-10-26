class Bateria:

    def __init__(self, capacidade:int):
        self.__capacidade:int = capacidade
        self.__carga:int = capacidade
    
    def __str__(self):
        return f"{self.__carga}/{self.__capacidade}"

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
    

class Notebook:

    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: None | Bateria = None

    
    def ligar(self):
        if self.__ligado == False and self.__bateria == None:
            print("Nao foi possivel ligar")

        elif self.__ligado == True:
            print("Notebook ja esta ligado")

        elif self.__ligado == False and bateria != None:
            self.__ligado = True
            print("notebook ligado")

    def desligar(self):
        if self.__ligado == False:
            print("Notebook ja esta desligado")
        else:
            self.__ligado = False

    def mostrar(self):

        if self.__ligado == True and self.__bateria != None:
            print(f"status: ligado, Bateria: ({self.__bateria.show()})")
       
        elif self.__ligado == False and self.__bateria == None:
            print("status: desligado, Bateria: Nenhuma")

        elif self.__ligado == False and self.__bateria != None:
            print(f"status: desligado, Bateria: ({self.__bateria.show()})")

    def usar(self, tempo:int):
        if self.__ligado == False:
            print("ligue o notebook para usar")
        else:
            self.__bateria.setCarga(tempo)

    
    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria





    



notebook = Notebook()
notebook.mostrar()
notebook.usar(10)
notebook.ligar()
notebook.mostrar()
bateria = Bateria(50)
bateria.show()
notebook.setBateria(bateria)
notebook.mostrar()
notebook.usar(10)
notebook.ligar()
notebook.mostrar()
notebook.usar(30)
notebook.mostrar()
notebook.ligar()
notebook.mostrar()
notebook.usar(30)
notebook.mostrar()
notebook.ligar()



