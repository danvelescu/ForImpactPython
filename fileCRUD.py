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
        fileRessurce.write("{" + "'name':" + self.Name + ",'price':" + str(self.Price) + ",'color':" + self.Color + "}")
        fileRessurce.close()


product1 = Product('asd', 2, "22")
