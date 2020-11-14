from repository import ClientRepository
from model import Client
class Bookshop:
    def __init__(self):
        self.clientRep = ClientRepository()
    def getClientById(self,id):
        client = self.clientRep.cautaDupaID(id)
        print(client.toString())

    def addClient(self,client):
        self.clientRep.adaugaClient(client)
    def printClients(self):
        self.clientRep.printAllClients()

bookshop = Bookshop()
bookshop.getClientById(2)

client=Client(201,218,"Ion Nistor")
bookshop.addClient(client)
bookshop.printClients()
