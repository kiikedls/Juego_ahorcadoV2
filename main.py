from os import system
from cListas import cListas
from cJuego import cJuego
from cConexion import cConexion
from verificar import verificar
from cGato import cGato


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
    print("""selecciona una de las siguientes opciones:
    1.-empezar a jugar
    2.-agregar una palabra
    3.-salir
    4.-reset""")
    
    n = int(input())
    if 1 == n:
        
        if verificar.verificar():
            palabras = data.llenar_lista()
            palabras = data.imprimir_listas()
            print(palabras)
        else:
            palabras = lista.llenar_lista()
            palabras = lista.imprimir_listas()
        ahorcado = cJuego()
        ahorcado.jugar(palabras)
        input()

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
        g=cGato()
        print("Bienvenido al gato!!")
        while code == 1:
            system("cls")
            opc = int(input("elige una opcion: "
                            "\n1.-empezar a jugar\n2.-salir\n"))
            if 1 == opc:
                system("cls")
                print("empieza el juego: ")
                for i in range(4):
                    print(' ' * 22),
                    for j in range(4):
                        print(g.getJuego()[i][j], end=" "),
                jg=g.quien_parte()
                print("\nEstas jugando contra la maquina, comienza "+jg)
                input("enter->")

                while True:
                    if jg == "el jugador":
                        pos=str(input("escribe la posicion para tu marca"
                              "(primero la letra, despues el numero)\n"))
                        system("cls")
                        print(g.jugada(jg,"X",pos.lower()))
                        #imprimir el gato
                        for i in range(4):
                            print(' ' * 22),
                            for j in range(4):
                                print(g.getJuego()[i][j], end=" "),
                        input("\nenter->")
                        if g.ganador(jg)=="ganador":
                            print("Has ganado "+jg)
                            input()
                            break
                        jg="el CPU"
                    elif jg=="el CPU":
                        system("cls")
                        print(g.CPU(jg,"O"))
                        #imprimir el gato
                        for i in range(4):
                            print(' ' * 22),
                            for j in range(4):
                                print(g.getJuego()[i][j], end=" "),
                        input("\nenter->")
                        if g.ganador(jg)=="ganador":
                            print("ha ganado "+jg)
                            input()
                            break
                        jg="el jugador"

            elif 2 == opc:
                code = -1

    if juego == 2:
        print("bienvenido al ahorcado")
        input()
        lista = cListas()
        data = cConexion()
        code = 1

        while code == 1:
            system("cls")
            print("selecciona una de las siguientes opciones: "
                  "\n1.-empezar a jugar\n2.-agregar una palabra"
                  "\n3.-salir\n4.-reset\n")
            #     print("""selecciona una de las siguientes opciones:
            # 1.-empezar a jugar
            # 2.-agregar una palabra
            # 3.-salir
            # 4.-reset""")
            n = int(input())
            if 1 == n:
                if verificar.verificar():
                    palabras = data.llenar_lista()
                    palabras = data.imprimir_listas()
                    print(palabras)
                else:
                    palabras = lista.llenar_lista()
                    palabras = lista.imprimir_listas()
                ahorcado = cJuego()
                ahorcado.jugar(palabras)
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
        token = False
print("Adios")
input()
