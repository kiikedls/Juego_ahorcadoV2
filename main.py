from os import system
from cListas import cListas
from cJuego import cJuego
from cConexion import cConexion
from verificar import verificar

print("bienvenido al ahorcado")
input()
lista = cListas()
data=cConexion()
code = 1

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
            palabras=data.imprimir_listas()
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
            palabras=data.llenar_lista()
            nueva = input("escribe la nueva palabra que quieres agregar al juego: ")
            data.nueva_palabra(nueva)
        else:
            palabras = lista.llenar_lista()
            nueva = input("escribe la nueva palabra que quieres agregar al juego: ")
            lista.nueva_palabra(nueva)
        # nueva = input("escribe la nueva palabra que quieres agregar al juego: ")
        # lista.nueva_palabra(nueva)
    elif 3 == n:
        code = -1
    elif 4 == n:
        if verificar.verificar():
            palabras=data.resetear()
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

print("hasta pronto")
input()
