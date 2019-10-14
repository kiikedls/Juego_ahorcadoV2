import pymysql
from random import shuffle


class cConexion:

    def __init__(self):
        # self.db = pymysql.connect('127.0.0.1', 'root', '', 'juego')
        # self.cursor = self.db.cursor()
        self.lista_destino = []

    def llenar_lista(self):
        self.db = pymysql.connect('127.0.0.1', 'root', '', 'juego')
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT `palabra` FROM palabras_destino")
        lista = self.cursor.fetchall()

        for i in lista:
            palabra = i[0]
            self.lista_destino.append(palabra)
        if len(self.lista_destino) == 0:
            self.cursor.execute("SELECT `palabra` FROM palabras_origen")
            lista = self.cursor.fetchall()
            for i in lista:
                palabra = i[0]
                self.lista_destino.append(palabra)
            shuffle(self.lista_destino)

        self.db.close()
        return self.lista_destino

    def imprimir_listas(self):
        name = self.lista_destino.pop()
        self.salva_palabra(name)
        return name

    def impPalabras(self):
        sqlq = 'SELECT * FROM palabras_origen'
        self.cursor.execute(sqlq)
        lista = self.cursor.fetchall()
        for i in lista:
            id = i[0]
            palabra = i[1]
            print("id: {0}, palabra: {1}"
                  .format(id, palabra))

        self.db.close()

    def salva_palabra(self,n):
        self.db = pymysql.connect('127.0.0.1', 'root', '', 'juego')
        self.cursor = self.db.cursor()
        self.cursor.execute('DROP TABLE `palabras_destino`')
        self.cursor.execute("""
                CREATE TABLE palabras_destino (id int auto_increment not null primary key, 
                palabra varchar(20) not null)""")

        for i in self.lista_destino:
            self.cursor.execute(f"INSERT INTO `palabras_destino`(`palabra`) VALUES('{i}')")
        self.db.commit()
        self.db.close()

    def nueva_palabra(self,p):
        self.db = pymysql.connect('127.0.0.1', 'root', '', 'juego')
        self.cursor = self.db.cursor()
        x=p
        self.cursor.execute(f"INSERT INTO `palabras_origen`(`palabra`) VALUES('{x}')")
        self.db.commit()
        self.db.close()
        print("palabra agregada con exito!")
        # listax=self.llenar_lista()
        # self.lista_destino.append(p)
        # self.salva_palabra(self.lista_destino)
        # for i in self.lista_destino:
        #     if listax[i]!=i:
        #         print(listax[i])
                # self.cursor.execute(f"INSERT INTO `palabra_origen`(`palabra`) VALUES({i})")

    def resetear(self):
        self.db = pymysql.connect('127.0.0.1', 'root', '', 'juego')
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT `palabra` FROM palabras_origen")
        lista=[]
        for i in self.cursor.fetchall():
            pal=i[0]
            lista.append(pal)
        shuffle(lista)


        self.cursor.execute("DROP TABLE `palabras_destino`")
        self.cursor.execute("""
        CREATE TABLE palabras_destino (id int auto_increment not null primary key, 
        palabra varchar(20) not null)""")
        for i in lista:
            self.cursor.execute(f"INSERT INTO `palabras_destino`(`palabra`) VALUES('{i}')")
        self.db.commit()
        self.db.close()
        return "lista reestablecida °w°"

#limpiar el codigo
#clases estaticas
#consulta para eliminar el ultimo registro
#agregar nombre
#