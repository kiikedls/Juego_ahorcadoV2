import random
class cGato:
    def __init__(self):
        self.matriz=[[' ','A','B','C'],['1','.','.','.'],['2','.','.','.'],['3','.','.','.']]
        self.game=[]

    def getJuego(self):
        return self.matriz

    def quien_parte(self):
        x=random.randrange(2)
        if x==1:
            parte="el jugador"
        else:
            parte="el CPU"
        return(parte)

    def jugada(self,jugador,z,pos):
        while True:
            x=None
            y=None
            entrada=pos
            for i in entrada:
                if i in "abc":
                    x="abc".index(i)+1
                    letra=i.upper()
                elif i in "123":
                    y=int(i)
                else:
                    break
            if self.matriz[y][x]==".":
                self.matriz[y][x]=z
                return(f"{jugador} ha marcado en {letra}{y}"+"\n")
            break

    def ganador(self, jugador):
        gana=False
        if self.matriz[1][1]==self.matriz[2][2]==self.matriz[3][3]!=".":
            gana=True
        elif self.matriz[1][3]==self.matriz[2][2]==self.matriz[3][1]!=".":
            gana=True
        elif self.matriz[1][1]==self.matriz[1][2]==self.matriz[1][3]!=".":
            gana=True
        elif self.matriz[2][1]==self.matriz[2][2]==self.matriz[2][3]!=".":
            gana=True
        elif self.matriz[3][1]==self.matriz[3][2]==self.matriz[3][3]!=".":
            gana=True
        elif self.matriz[1][1]==self.matriz[2][1]==self.matriz[3][1]!=".":
            gana=True
        elif self.matriz[1][2]==self.matriz[2][2]==self.matriz[3][2]!=".":
            gana=True
        elif self.matriz[1][3]==self.matriz[2][3]==self.matriz[3][3]!=".":
            gana=True
        if gana:
            return "ganador"

    def CPU(self,jugador,z):
        x=random.randrange(1,4)
        y=random.randrange(1,4)
        if self.matriz[y][x]==".":
            self.matriz[y][x]=z
            if x==1:
                letra="A"
            elif x==2:
                letra="B"
            elif x==3:
                letra="C"
            return (f"{jugador} ha marcado en {letra}{y}")