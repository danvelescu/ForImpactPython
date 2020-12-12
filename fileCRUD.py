import json

class Product:
    def __init__(self, name, price, color):
        self.Name = name
        self.Price = price
        self.Color = color
        if (name == '' and price == '' and color == ''):
            self.SaveProduct()

    def SaveProduct(self):
        self.Name = input('Введите название продукта ')
        try:
            self.Price = int(input('Введите цену продукта'))
        except ValueError:
            print('Неверный тип данных')
            self.SaveProduct()
        self.Color = input('Введите цвет продукта')
        fileRessurce = open("NameOfProducts.txt", "a")
        fileRessurce.write('{"name":"'+self.Name+'",'+'"price":"'+str(self.Price)+'",'+'"color":"'+str(self.Color)+'"}\n')
        fileRessurce.close()

    def deleteAll(self):
        try:
            fileRessurse = open("NameOfProducts.txt","w")
        except:
            print("file not exists!!!")
        fileRessurse.write("")
        fileRessurse.close()


    def jsonToProduct(self):
        fileResource = open("NameOfProducts.txt","r")
        products = []
        for product in fileResource:
            p = json.loads(product)
            products.append(Product(p['name'],p['price'],p['color']))
        fileResource.close()
        return products



    def printMyProduct(self):
        for product in self.jsonToProduct():
            print(product.Color)

    def summpriceProducts(self):
        products = self.jsonToProduct()
        summ = 0
        for product in products:
            summ += int(product.Price)
        print(summ)


#user interface menu
#buy products and 2 chouses






x = '{"name":"sadas","price":"123","color":"qwe"}'

eu = json.loads(x)

print(eu['color'])


product1 = Product("1","1","1")

product1.summpriceProducts()







