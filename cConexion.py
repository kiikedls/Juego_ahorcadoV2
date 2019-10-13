import pymysql
from random import shuffle

class cConexion:
    def __init__(self):
        self.db=pymysql.connect('127.0.0.1','root','','juego')
        self.cursor=self.db.cursor()

    def impPalabras(self):
        sqlq='SELECT * FROM palabras_origen'
        self.cursor.execute(sqlq)

        lista=self.cursor.fetchall()
        for i in lista:
            id=i[0]
            palabra=i[1]
            print("id: {0}, palabra: {1}"
                  .format(id,palabra))

        self.db.close()

    def desordena(self):
        lista_destino=[]
        sqlq = 'SELECT * FROM palabras_origen'
        self.cursor.execute(sqlq)

        lista = self.cursor.fetchall()
        for i in lista:
            id = i[0]
            palabra = i[1]
            lista_destino.append(palabra)

        shuffle(lista_destino)
        print(lista_destino)

        for j in lista_destino:
            self.cursor.execute(f"INSERT INTO `palabras_destino`(`palabra`) VALUES('{j}')")
            print(j)
        self.db.commit()
        print("pudrete flanders")
        self.db.close()
