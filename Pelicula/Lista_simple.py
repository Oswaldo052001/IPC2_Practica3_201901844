from Pelicula.Nodo import Nodo


class ListaSimple():
    id = 0
    def __init__(self):
        self.nodoInicio = None
        self.nodoFinal = None
        self.size = 0

    def getInicio(self):
        return self.nodoInicio
    
    def getFin(self):
        return self.nodoFinal

    def estaVacia(self):
        return self.nodoInicio == None

    def agregarFinal(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        else:
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        self.size += 1

    def agregarInicio(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        else:
            nuevo.setSiguiente(self.nodoInicio)
            self.nodoInicio = nuevo
        self.size += 1

    def imprimir(self):
        tmp = self.nodoInicio
        while tmp:
            print(tmp.getDato())
            tmp = tmp.getSiguiente()
