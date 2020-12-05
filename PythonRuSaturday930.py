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






class Phone:
    model = ''
    series = ''
    color = ''
    clients = ''


phone1 = Phone()
phone2 = Phone()
phone3 = Phone()
phone4 = Phone()
phone5 = Phone()
phone16 = Phone()

phone1.series = "mi2"

text = "text"
nomer = 1
nomer = str(phone1)

print(text+nomer)

