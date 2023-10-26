from Pelicula.objPelicula import peli

class operaciones():
    def __init__(self, listaPeliculas) -> None:
        self.listaPeliculas = listaPeliculas



    def InsertarPelicula(self,id, nombre, genero):
        if self.IdUnico(id):
            tmpPeli = peli(id,nombre,genero)   # Creando objeto sistema que hay en el xml
            self.listaPeliculas.agregarFinal(tmpPeli)  # Agregando sistema a la lista de sistemas
            return ("Se guardo Correctamente")
        else:
            return ("Id existente")
        
    def ActualizarPelicula(self,id, nombre, genero):
        peli = self.listaPeliculas.getInicio()
        actualizado = False
        while peli:
            if peli.getDato().getID() == id:
                actualizado = True
                peli.getDato().setName(nombre)
                peli.getDato().setGenero(genero)
            peli = peli.getSiguiente()
        if actualizado == True:
            return ("Se actualizó Correctamente")
        else:
            return ("No se encontró el Id")
        
    def IdUnico(self, id):
        unico = True
        peli = self.listaPeliculas.getInicio()
        while peli:
            if peli.getDato().getID() == id:
                unico = False
            peli = peli.getSiguiente()
        return unico
    
    def comprobrar(self):
        peli = self.listaPeliculas.getInicio()
        while peli:
            print(peli.getDato().getName())
            peli = peli.getSiguiente()
    
