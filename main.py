a = [10, 122, 123, 231, 213, 1324, 1234, 213, 124, 124, 124, 124, 124, 124, 124, 124, 124, 34, 3, 543, 53, 452, 4132,
     4132]
a.append(99)
a.append(29)
a.append(311)
print(len(a))

drugoiSpisok = []

for number in a:
    if number % 3 == 0:
        drugoiSpisok.append(number)

# cacoi tip spisca ?
# int
# cocaia dlina?
# 10
# cito tam dobaviti?
# vivodit na ecran
typeOflist = input("какой тип данных")
lenoflist = int(input("дай мне длинну списка"))

spisok = []

if typeOflist == "int":
    typeOflist = type(1)

if type(lenoflist) == type(1):
    for i in range(lenoflist):
        element = int(input("добавь элемент"))
        if typeOflist == type(element):
            spisok.append(element)
        else:
            print("Ti ne dobavil preavilino daniie")
else:
    print("Ti ne pravilino napisal dlinu spiska")


print(spisok)