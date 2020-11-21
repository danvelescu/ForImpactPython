class Parcare:
    id = 0

    def __init__(self, pret):
        self.pret = pret
        self.locuri = LocuriRepositorry()

    def OcupaLocul(self):
        self.locuri.afiseazalocuri()
        loc_id = int(input("Alege un loc : "))
        for loc in self.locuri.lista_de_locuri:
            if loc.id == loc_id:
                if loc.ocupat == False:
                    nume = input("Introdu numele: ")
                    prenume = input("Introdu prenumele: ")
                    client = Client(self.id, nume, prenume)
                    self.id += 1
                    loc.ocupat = True
                    loc.client = client

    def elibereazaLocul(self,id_client):
        for loc in self.locuri.lista_de_locuri:
            if loc.client.id == id_client:
                loc.ocupat = False
                loc.client = None




class LocuriRepositorry:
    def __init__(self):
        self.lista_de_locuri = [
            Loc(1),
            Loc(2),
            Loc(3),
            Loc(4),
            Loc(5),
            Loc(6),
            Loc(7)
        ]

    def afiseazalocuri(self):
        for loc in self.lista_de_locuri:
            print("Loc id: " + str(loc.id) + " Ocupat: " + str(loc.ocupat))
            if loc.ocupat == True:
                print("Nume: "+loc.client.nume+" Prenume: "+loc.client.prenume)



class Loc:
    def __init__(self, id):
        self.id = id
        self.ocupat = False
        self.client = Client(-1,"","")


class Client:
    def __init__(self, id, nume, prenume):
        self.id = id
        self.nume = nume
        self.prenume = prenume




parcare1 = Parcare(5)

parcare1.OcupaLocul()

parcare1.locuri.afiseazalocuri()


parcare1.elibereazaLocul(0)
print("----------------------------------------")
parcare1.locuri.afiseazalocuri()