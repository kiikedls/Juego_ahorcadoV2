import pymysql
from random import shuffle


class cListas:
    def __init__(self):
        self.lista = []
        self.record=[]

    def llenar_lista(self):
        self.lista = [line.rstrip() for line in open("lista_destino.txt",encoding='utf-8')]
        if len(self.lista) == 0:
            self.lista = [line.rstrip() for line in open("lista_origen.txt",encoding='utf-8')]
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
        self.lista.append(palabra)
        self.salva_palabras(self.lista)
        self.guardar = open("lista_origen.txt", "w", encoding="utf-8")
        self.cadena = "\n".join(str(x) for x in self.lista)
        self.guardar.write(self.cadena)
        self.guardar.close()
        return "palabra agregada con exito"
        # if not re.fullmatch(r"[A-Za-z ]{1,15}", palabra)

    def resetear(self):
        self.lista = [line.rstrip() for line in open("lista_origen.txt")]
        shuffle(self.lista)
        self.guardar = open("lista_destino.txt", "w", encoding="utf-8")
        self.cadena = "\n".join(str(x) for x in self.lista)
        self.guardar.write(self.cadena)
        self.guardar.close()
        return "lista de palabras reseteada °w°"

    def eliminar_BD(self):
        try:
            self.db = pymysql.connect('127.0.0.1', 'root', '', 'juego')
            self.cursor = self.db.cursor()
            self.cursor.execute("SELECT `palabra` FROM palabras_destino")
            l = []
            for x in self.cursor.fetchall():
                pal = x[0]
                l.append(pal)
            
            self.destino = [linea.rstrip() for linea in open("lista_destino.txt")]
            

            for i,e in enumerate(l):
                if e not in self.destino:
                    self.cursor.execute(f"DELETE FROM `palabras_destino` WHERE (`palabra` = '{e}')")
            self.db.commit()
            self.db.close()     
        except Exception as e:
            pass

    def score(self, nombre, agame,apuntos, ggame, gpuntos):
        reg=[line.rstrip() for line in open("jugadores.txt",encoding='utf-8')]
        print(reg)
        input()
        cadena=[nombre+"-"+str(agame)+"-"+str(apuntos)+"-"+str(ggame)+"-"+str(gpuntos)]
        print(cadena)
        input()
        reg.extend(cadena)
        print(reg)
        input()
        # "\n".join(str(x) for x in self.lista)
        guardar=open("jugadores.txt", "w", encoding="utf-8")
        cad="\n".join(str(x) for x in reg)
        print(cad)
        input()
        guardar.write(cad)
        guardar.close()
        return [[line.rstrip()] for line in open("jugadores.txt",encoding='utf-8')]