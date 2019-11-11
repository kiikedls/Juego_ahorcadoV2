from os import system
from cListas import cListas
from cJuego import cJuego
from cConexion import cConexion
from verificar import verificar
from cGato import cGato

print("Nombre del jugador")
nombre = ""
nombre = input("")
Ggame = 0
Agame=0
puntos = 0
Gpuntos = 0
Apuntos = 0

lista = cListas()
data = cConexion()
g = cGato()
code = 2
try:
    if verificar.verificar():
        lista.eliminar_BD()
        data.eliminar_txt()
        while len(nombre) == 0:
            if len(nombre) > 0:
                data.agregar_nombre(nombre)
            else:
                system("cls")
                print("Nombre del jugador")
                nombre = input("")
        data.agregar_nombre(nombre)
except Exception as e:
    pass

system("cls")
token = True
while token:
    system("cls")
    print((">bienvenido a los juegos de juan<".title()).center(50, "=") + "\n")
    juego = int(input("elige el juego que deseas jugar: "
                      "\n1.-gato\n2.-ahorcado\n3.-salir\n"))
    if juego == 1:
        system("cls")
        code = 1

        print("Bienvenido al gato!!")
        while code == 1:
            system("cls")
            opc = int(input("elige una opcion: "
                            "\n1.-empezar a jugar\n2.-salir\n"))
            if 1 == opc:
                system("cls")
                Ggame = Ggame + 1
                try:
                    data.gato(Ggame,puntos)
                except Exception as e:
                    pass
                # data.gato(Ggame,puntos)
                print("empieza el juego: ")
                for i in range(4):
                    print(' ' * 22),
                    for j in range(4):
                        print(g.getJuego()[i][j], end=" "),
                jg = g.quien_parte()
                print("\nEstas jugando contra la maquina, comienza " + jg)
                input("enter->")

                while True:
                    if jg == "el jugador":
                        pos = str(input("escribe la posicion para tu marca"
                                        "(primero la letra, despues el numero)\n"))
                        while len(pos) == 0:
                            pos = str(input("escribe la posicion para tu marca"
                                            "(primero la letra, despues el numero)\n"))
                        while len(pos) > 0:
                            if pos[0] in "abc" and pos[1] in "123":
                                system("cls")
                                print(g.jugada(jg, "X", pos.lower()))
                                break
                            else:
                                pos = str(input("escribe la posicion para tu marca"
                                                "(primero la letra, despues el numero)\n"))
                            while len(pos) == 0:
                                pos = str(input("escribe la posicion para tu marca"
                                                "(primero la letra, despues el numero)\n"))

                        # imprimir el gato
                        for i in range(4):
                            print(' ' * 22),
                            for j in range(4):
                                print(g.getJuego()[i][j], end=" "),
                        input("\nenter->")
                        if g.ganador(jg) == "ganador":

                            Gpuntos = Gpuntos + 1
                            data.gato(Ggame,Gpuntos)

                            puntos = puntos + 1
                            try:
                                data.gato(Ggame,puntos)
                            except Exception as e:
                                pass

                            print("Has ganado " + jg)
                            input()
                            puntos = puntos + 1
                            g.reset()
                            break
                        jg = "el CPU"
                    elif jg == "el CPU":
                        system("cls")
                        print(g.CPU(jg, "O"))
                        # imprimir el gato
                        for i in range(4):
                            print(' ' * 22),
                            for j in range(4):
                                print(g.getJuego()[i][j], end=" "),
                        input("\nenter->")
                        if g.ganador(jg) == "ganador":
                            print("ha ganado " + jg)
                            input()
                            break
                        jg = "el jugador"

            elif 2 == opc:
                code = -1
                Ggame = 0

    if juego == 2:
        system("cls")
        print("bienvenido al ahorcado")
        input()
        lista = cListas()
        data = cConexion()
        code = 1
        try:
            if verificar.verificar():
                lista.eliminar_BD()
                data.eliminar_txt()
        except Exception as e:
            pass
        while code == 1:
            system("cls")
            print("selecciona una de las siguientes opciones: "
                  "\n1.-empezar a jugar\n2.-agregar una palabra"
                  "\n3.-salir\n4.-reset\n")

            n = int(input())
            if 1 == n:

                if verificar.verificar():
                    palabras = data.llenar_lista()
                    palabras = data.imprimir_listas()
                    print(palabras)
                    Ggame = Ggame + 1

                    data.ahorcado(Ggame,Apuntos)

                    try:
                        data.ahorcado(Ggame,puntos)
                    except Exception as e:
                        pass
                else:
                    palabras = lista.llenar_lista()
                    palabras = lista.imprimir_listas()
                system("cls")
                print("tienes 5 intentos para adivinar la palabra oculta antes de quedar ahorcado.")
                ahorcado = cJuego()
                if ahorcado.jugar(palabras)==True:
                    puntos=puntos+1
                    Apuntos = Apuntos + 1
                    try:
                        data.ahorcado(Ggame,Apuntos)
                    except Exception as e:
                        pass
                    print("has ganado!!! ^o^")
                else:
                    print("has perdido :(")
                Agame = Agame + 1
                print(Agame)
                input()
            elif 2 == n:
                system("cls")
                if verificar.verificar():
                    palabras = data.llenar_lista()
                    nueva = input("escribe la nueva palabra que quieres agregar al juego: ")
                    data.nueva_palabra(nueva)
                else:
                    palabras = lista.llenar_lista()
                    nueva = input("escribe la nueva palabra que quieres agregar al juego: ")
                    lista.nueva_palabra(nueva)
            elif 3 == n:
                code = -1
            elif 4 == n:
                if verificar.verificar():
                    palabras = data.resetear()
                else:
                    palabras = lista.resetear()
                print(palabras)
                input()
            elif 5 == n:
                dibujito = cJuego()
                n2 = int(input("num errores: "))
                print(dibujito.errores(n2))
                input()
            else:
                system("cls")
                print("numero invalido")
                input()
        input("hasta pronto.")
    if juego == 3:
        try:
            data.ahorcado(Ggame,Apuntos)
        except Exception as e:
            pass
        lista.score(nombre,Agame,Ggame,puntos)
        token = False
print("Adios")
input()
