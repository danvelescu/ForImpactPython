# spisko = ['1', '.', '1', '2', '.', '22', 'aa']
#
#
# def filterList(list):
#     spisko = []
#     for element in list:
#         if element == '.':
#             spisko.append(" ")
#         else:
#             spisko.append(element)
#     return spisko
#
#
# spisko = filterList(spisko)
#
# print(spisko)
#
# lis1 = [
#     'a23',
#     'b2',
#     '1',
#     'att',
#     'zt',
#     '1231',
# ]
#
#
# def filterList_lenNum(list):
#     spisok = []
#     for word in list:
#         if len(word) >= 3:
#             spisok.append(word[0])
#         else:
#             spisok.append(word)
#     return spisok
#
#
# lis1 = filterList_lenNum(lis1)
#
# print(lis1)
#
# phone = {
#     "model": "Iphone",
#     "series": "XII",
#     "color": "Grey",
#     "clients": {
#         "client1": {"name": "dan", "surname": "velescu"},
#         "client2": {"name": "dan", "surname": "velescu"},
#         "client3": {"name": "dan", "surname": "velescu"},
#         "client4": {"name": "dan", "surname": "velescu"},
#         "client5": {"name": "dan", "surname": "velescu"},
#     }
# }
#
# phones = {
#     "phones": {
#         "phone1": {"model": "Iphone",
#                    "series": "XII",
#                    "color": "Grey",
#                    "clients": {
#                        "client1": {"name": "dan", "surname": "velescu"},
#                        "client2": {"name": "dan", "surname": "velescu"},
#                        "client3": {"name": "dan", "surname": "velescu"},
#                        "client4": {"name": "dan", "surname": "velescu"},
#                        "client5": {"name": "dan", "surname": "velescu"}
#                    }
#                    },
#         "phone2": {
#             "model": "Iphone",
#             "series": "XII",
#             "color": "Grey",
#             "clients": {
#                 "client1": {"name": "dan", "surname": "velescu"},
#                 "client2": {"name": "dan", "surname": "velescu"},
#                 "client3": {"name": "dan", "surname": "velescu"},
#                 "client4": {"name": "dan", "surname": "velescu"},
#                 "client5": {"name": "Maxim", "surname": "velescu"}
#             }
#         }
#     }
# }
#
# print(phones["phones"]["phone2"]["clients"]["client5"]["name"])


#
#

class Phone:
    model = ''
    series = ''
    color = ''
    clients = ''


#
# phone1 = Phone()
# phone2 = Phone()
# phone3 = Phone()
# phone4 = Phone()
# phone5 = Phone()
# phone16 = Phone()
#
# phone1.series = "mi2"
#
# text = "text"
# nomer = 1
# nomer = str(phone1)
#
# print(text+nomer)
# spisok = range(1,11)
#
# thisset = {"a", "b", "c","d"}
# phone = Phone()
# print("sadasd"-10)
#
# for element in thisset:
#     print(element)
#
# print(thisset)

import random

list1 = [5, 1, 54, 6, 1, 3, 6, 8, 2, 5, 46]
list2 = []
results = []

for nr in range(11):
    list2.append(random.randint(2, 10))

for nr in range(11):
    results.append(int(list1[nr] / list2[nr]))



print(results)
factorialResults = []
for nr in results:
    if nr == 0:
        factorialResults.append(0)
        continue
    elif nr == 1:
        factorialResults.append(1)
        continue
    summ=1
    while nr > 0:
        summ*=nr
        nr-=1
    factorialResults.append(summ)

print(factorialResults)


"Создать программу с функциями, которые задают 5 вопросов про человека и сохраняют всё в формате json. \
Создаётся ещё одна программа, где используется написанный выше модуль. Через аргументы будут передаваться данные."
