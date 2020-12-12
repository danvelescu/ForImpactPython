class Product:
    # def __init__(self, name, price, color):
    #     self.Name = name
    #     self.Price = price
    #     self.Color = color
    #     if (name == '' and price == '' and color == ''):
    #         self.SaveProduct()

    def SaveProduct(self):
        self.Name = input('Введите название продукта ')
        try:
            self.Price = int(input('Введите цену продукта'))
        except ValueError:
            print('Неверный тип данных')
            self.SaveProduct()
        self.Color = input('Введите цвет продукта')
        fileRessurce = open("NameOfProducts.txt", "a")
        fileRessurce.write('\n{"name":"'+self.Name+'",'+'"price":"'+str(self.Price)+'",'+'"color":"'+str(self.Color)+'"}')
        fileRessurce.close()

    # def deleteAll(self):

x = '{"name":"dd","price":123,"color":"sd"}'




product1 = Product()
product1.SaveProduct()


import json




eu = json.loads(x)

print(eu['name'])


