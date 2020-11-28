



class XO:
    menutext = ("play", "menu", "exit")
    checknumber = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    global selectedMenuItem

    def MainMenu(self):
        print("_____________")
        print("|_%s_|_%s_|_%s_|"%(1,2,3))
        print("|_%s_|_%s_|_%s_|"%(4,5,6))
        print("|_%s_|_%s_|_%s_|"%(7,8,9))
        print("Welcome Impacter ")
        print("-play")
        print("-menu")
        print("-exit")

        self.selectedMenuItem = input("Type comand:")

        while self.selectedMenuItem not in self.menutext:
            print("Type comand:")
            self.selectedMenuItem = input("")

        if(self.selectedMenuItem == 'play'):
            self.play_game()

    def play_game(self):
        def Render(field):
            print("|_%s_|_%s_|_%s_|"%(field[0],field[1],field[2])," "*5,
                  "|_%s_|_%s_|_%s_|" % (1, 2, 3))
            print("|_%s_|_%s_|_%s_|" % (field[3], field[4], field[5]), " " * 5,
                  "|_%s_|_%s_|_%s_|" % (4, 5, 6))
            print("|_%s_|_%s_|_%s_|" % (field[6], field[7], field[8]), " " * 5,
                  "|_%s_|_%s_|_%s_|" % (7, 8, 9))


        def listenType(pl):
            print("You(%s):"%pl)
            global numberImput
            numberImput = input("")
            while numberImput not in self.checknumber:
                print("Type correct number 1-9")
                numberImput = input("")




game = XO()
game.MainMenu()