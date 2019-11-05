from os import system


class cJuego:
    def __init__(self):
        self.ner = 0
        self.lis = []
        self.aciertos = []

    def jugar(self, palabra):
        self.lis.extend(palabra)
        x = "_"
        llave = True
        self.aciertos.extend("_" * len(self.lis))

        while llave:
            system("cls")
            print("tienes 5 intentos para adivinar la palabra oculta antes de quedar ahorcado.")
            print(self.errores(self.ner))
            if len(self.aciertos) == 0:
                print("_ " * len(self.lis))
            elif self.aciertos.count("_") == 0:
                print("has ganado!!! ^o^")
                return
            else:
                print(self.aciertos)
            p = input("introduce una letra: ")

            if self.lis.count(p) != 0:
                for i, val in enumerate(self.lis):
                    if val == p:
                        self.aciertos[i] = val
                    elif val != p and val != "_":
                        self.aciertos[i] = self.aciertos[i]
                    else:
                        self.aciertos[i] = x
                print(self.aciertos)
            elif self.ner > 3:
                system("cls")
                print(self.errores(5))
                # input()
                print("has perdido :(")
                return
            else:
                print("error, esa letra no forma parte de la palabra")
                self.ner += 1
                input("enter->")

    def errores(self, e):
        switcher = {
            0: """              __________
                        |
                        |
                        |
                        |
                        |
                        |
            ____________|_""",
            1: """              __________
             |          |
             |          |
                        |
                        |
                        |
                        |
            ____________|_""",
            2: """              __________
             |          |
             |          |
             O          |
                        |
                        |
                        |
            ____________|_""",
            3: """              __________
             |          |
             |          |
             O          |
             |          |
                        |
                        |
            ____________|_""",
            4: """              __________
             |          |
             |          |
             O          |
            /|\         |
                        |
                        |
            ____________|_""",
            5: """              __________
             |          |
             |          |
             O          |
            /|\         |
            / \         |
                        |
            ____________|_
            Game Over."""
        }
        return switcher.get(e, "excepcion no controlada")
