from random import shuffle


class cListas:
    def __init__(self):
        self.lista = []

    def llenar_lista(self):
        self.lista = [line.rstrip() for line in open("lista_destino.txt")]
        if len(self.lista) == 0:
            self.lista = [line.rstrip() for line in open("lista_origen.txt")]
            shuffle(self.lista)
        return self.lista

    def salva_palabras(self, lista):
        self.guardar = open("lista_destino.txt", "w", encoding="utf-8")
        self.cadena = "\n".join(str(x) for x in lista)
        self.guardar.write(self.cadena)
        self.guardar.close()

    def imprimir_listas(self):
        name = self.lista.pop()
        self.salva_palabras(self.lista)
        return name

    def nueva_palabra(self, palabra):
        self.llenar_lista()
        self.lista.append(palabra)
        self.salva_palabras(self.lista)
        self.guardar = open("lista_origen.txt", "w", encoding="utf-8")
        self.cadena = "\n".join(str(x) for x in self.lista)
        self.guardar.write(self.cadena)
        self.guardar.close()
        print("palabra agregada con exito", self.lista)
        # if not re.fullmatch(r"[A-Za-z ]{1,15}", palabra)

    def resetear(self):
        self.lista = [line.rstrip() for line in open("lista_origen.txt")]
        shuffle(self.lista)
        self.guardar = open("lista_destino.txt", "w", encoding="utf-8")
        self.cadena = "\n".join(str(x) for x in self.lista)
        self.guardar.write(self.cadena)
        self.guardar.close()
        return "lista de palabras reseteada °w°"
