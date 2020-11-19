class Book:
    def __init__(self,id,name,author,price):
        self.id = id
        self.name = name
        self.author = author
        self.price = price




class BookShop:
    def __init__(self,name):
        self.name = name
        self.repository = BookRepository()


    def cumparaCartea(self,id):
        for book in self.repository.listOfBooks:
            if book.id == id:
                print("Ai luat cartea")
                print("Name "+book.name)
        self.repository.deleteBookById(id)



class BookRepository:
    def __init__(self):
       self.listOfBooks = [
            Book(1, "Micu Print", "Antonio S.", "150 lei"),
            Book(2, "Micu Print", "Antonio S.", "150 lei"),
            Book(3, "Micu Print", "Antonio S.", "150 lei"),
            Book(4, "Micu Print", "Antonio S.", "150 lei"),
            Book(5, "Game of thrones", "Antonio S.", "150 lei"),
            Book(6, "Micu Print", "Antonio S.", "150 lei"),
            Book(7, "Micu Print", "Antonio S.", "150 lei"),
            Book(8, "Micu Print", "Antonio S.", "150 lei"),
            Book(9, "Micu Print", "Antonio S.", "150 lei"),
            Book(10, "Micu Print", "Antonio S.", "150 lei"),
            Book(11, "Micu Print", "Antonio S.", "150 lei"),
            Book(12, "Micu Print", "Antonio S.", "150 lei"),
            Book(13, "Micu Print", "Antonio S.", "150 lei"),
            Book(14, "Micu Print", "Antonio S.", "150 lei"),
            Book(15, "Micu Print", "Antonio S.", "150 lei"),
            Book(16, "Micu Print", "Antonio S.", "150 lei")
        ]

    def deleteBookById(self,id):
        for book in self.listOfBooks:
            if book.id == id:
                self.listOfBooks.remove(book)

    def afusarelistadecarti(self):
        for book in self.listOfBooks:
            print(book)


bookshop1 = BookShop("Caturesti")


bookshop1.cumparaCartea(5)

bookshop1.repository.afusarelistadecarti()