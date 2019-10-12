from os import system
from cListas import cListas
from cJuego import cJuego

print("bienvenido al ahorcado")
input()
lista = cListas()
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
        palabras = lista.llenar_lista()
        palabras = lista.imprimir_listas()
        ahorcado = cJuego()
        ahorcado.jugar(palabras)
        input()

    elif 2 == n:
        system("cls")
        palabras = lista.llenar_lista()
        nueva = input("escribe la nueva palabra que quieres agregar al juego: ")
        lista.nueva_palabra(nueva)
    elif 3 == n:
        code = -1
    elif 4 == n:
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