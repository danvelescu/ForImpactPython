class Book:
    def __init__(self,id,name,autor,status,price):
        self.name=name
        self.autor=autor
        self.status=status
        self.id=id
        self.price=price

class Client:
    def __init__(self,id,lei,adress , name ,surname):
        self.id = id
        self.cash=lei
        self.adress=adress
        self.name = name
        self.surname = surname

    def toString(self):
        return "{id:"+str(self.id)+\
               ",bani:"+str(self.cash)+\
               ",adress: "+self.adress+\
               ",name:  "+self.name+\
               ",surname: "+self.surname+"}"











