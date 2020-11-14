from model import Client,Book


class ClientRepository:
    lista_de_clienti = [
        Client(1,500,"Chisinau-Grenoble"),
        Client(2,1000,"Chisinau-Banulescu Bodonii"),
        Client(3, 0, "Soroca-Strada Sorocii"),
        Client(4,1000, "Briceni-Strada victoriei 1/2"),
        Client(5, 50000, "Chisinau-Grenoble")
    ]

    def adaugaClient(self,client):
        self.lista_de_clienti.append(client)

    def cautaDupaID(self,id):
        for client in self.lista_de_clienti:
            if id == client.id:
                return client

    def printAllClients(self):
        for client in self.lista_de_clienti:
            print(client.toString())

class BookRepository:
    lista_de_carti = [
        Book(1,"Harry Potter si piatra filosofala","J.K.Rowling","Valid",250),
        Book(2,"Amintiri din copilarie","Ion Creanga","Valid",50),
        Book(3,"Tabloul","Agatha Cristie","NanStock",95),
        Book(4,"Copii Capitanului Grant 1","Jules Verne","Valid",105),
        Book(5,"Enciclopedia Stiintelor","Editura:impact","Valid",59),
        Book(6,"Dictionar Roman-Englez","Editura:StudyEnglish","Valid",126)
]