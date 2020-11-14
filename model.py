class Book:
    def __init__(self,id,name,autor,status,price):
        self.name=name
        self.autor=autor
        self.status=status
        self.id=id
        self.price=price

class Client:
    def __init__(self,id,bani,adress):
        self.id = id
        self.cash=bani
        self.adress=adress

    def toString(self):
        return "{id:"+str(self.id)+",bani:"+str(self.cash)+",adress: "+self.adress+"}"











