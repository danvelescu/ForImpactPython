from model import Client,Book


class ClientRepository:
    lista_de_clienti = [
        Client(1,500,"Chisinau-Grenoble", "Marcel", "Tri"),
        Client(2,1000,"Chisinau-Banulescu Bodonii", "Anton", "Solomon"),
        Client(3, 0, "Soroca-Strada Sorocii", "Roman", "Canibal"),
        Client(4,1000, "Briceni-Strada victoriei 1/2", "Ion", "Batan"),
        Client(5, 50000, "Chisinau-Grenoble", "Simion", "Caprosu")
    ]
    def GetClientById(self,id):
        for client in self.lista_de_clienti:
            if client.id == id:
                return client

    def addClient(self,clienttoadd):
        for client in self.lista_de_clienti:
            if client.id == clienttoadd.id:
                print("client esti")
        else:
            self.lista_de_clienti.append(clienttoadd)




class BookRepository:
    lista_de_carti = [
        Book(1,"Harry Potter si piatra filosofala","J.K.Rowling","Valid",250),
        Book(2,"Amintiri din copilarie","Ion Creanga","Valid",50),
        Book(3,"Tabloul","Agatha Cristie","NanStock",95),
        Book(4,"Copii Capitanului Grant 1","Jules Verne","Valid",105),
        Book(5,"Enciclopedia Stiintelor","Editura:impact","Valid",59),
        Book(6,"Dictionar Roman-Englez","Editura:StudyEnglish","Valid",126)
]