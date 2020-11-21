# a = [10, 122, 123, 231, 213, 1324, 1234, 213, 124, 124, 124, 124, 124, 124, 124, 124, 124, 34, 3, 543, 53, 452, 4132,
#      4132]
# a.append(99)
# a.append(29)
# a.append(311)
# print(len(a))
#
# drugoiSpisok = []
#
# for number in a:
#     if number % 3 == 0:
#         drugoiSpisok.append(number)
#
# # cacoi tip spisca ?
# # int
# # cocaia dlina?
# # 10
# # cito tam dobaviti?
# # vivodit na ecran
# typeOflist = input("какой тип данных")
# lenoflist = int(input("дай мне длинну списка"))
#
# spisok = []
#
# if typeOflist == "int":
#     typeOflist = type(1)
#
# if type(lenoflist) == type(1):
#     for i in range(lenoflist):
#         element = int(input("добавь элемент"))
#         if typeOflist == type(element):
#             spisok.append(element)
#         else:
#             print("Ti ne dobavil preavilino daniie")
# else:
#     print("Ti ne pravilino napisal dlinu spiska")
#
#
# print(spisok)
#
#
# boolean1 = True
# int1 = 1
# float1 = 1.111
# str1 = "sss"
# boolean3 = True
#
# print(str1)
#
# # List
# list1 = [1, 2, "sdadsa"]
# list1[0]
#
# # Tuple
# tupleList = (1, 2, 3, 4, 45)
# # tupleList[1] = 10
#
# # Set
# setList = {1, 1, "da", "da"}
# setList.add("da")
#
# dictionary
# dict1 = {"key": "value", "key1": "value1", 1: "one", 1.23444: "asdasd"}
#
#
#
#
#
# car = {
#     "color":"Red",
#     "Year":"2016",
#     "Model":"Tesla",
#     "Series":"S",
#     "clients":["dan","klim","Diana","Alexei"]
# }
#
#
# print(car["color"])
#
# for element in dict1:
#     print(dict1[element])
#

#
#
# spisok1 = [1,213,43,34,234,235,135,235,1234,12]
# spisok2 = [2,314,23,4324,213,1323,1123,1213,1253,1263,1238]
# spisok3 = [2,314,23,4324,213,123,123,123,123,123,123]
# spisok4 = [2,314,23,4324,213,123,123,123,123,123,123]
# spisok5 = [2,314,23,4324,213,123,123,123,123,123,123]
#
#
# def filterEvenNumbers(list):
#     for nr in list:
#         if nr % 2 != 0:
#             list.remove(nr)
#     print(list)
#
#
# filterEvenNumbers(spisok4)

import random

def giveMeANumber():
    number = random.randint(1,100)
    return number



print(giveMeANumber())
