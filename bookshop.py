from repository import ClientRepository
from model import Client
class Bookshop:
    def __init__(self):
        self.clientRep = ClientRepository()

    def GetClientById(self,id):
        a = self.clientRep.GetClientById(id)
        return a
    def AddNewClient(self,client):
        self.clientRep.addClient(client)


shop = Bookshop()
client = shop.GetClientById(1)
client1 = Client(420,699,"odin","artiom","pupkin")
shop.AddNewClient(client1)
shop.AddNewClient(client)
print(client.toString())


