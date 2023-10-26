
class peli():

    def __init__(self,id,name,genero):
        self.id = id
        self.name = name
        self.genero = genero
    
    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getGenero(self):
        return self.genero
    
    def setId(self, id):
        self.id = id
        
    def setName(self, nam):
        self.name = nam

    def setGenero(self, gen):
        self.genero = gen