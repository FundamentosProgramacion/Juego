#Encoding:UTF-8
#Autor:Paola Castillo Nacif
#Proyecto final: Juego "Snake"

from Graphics import*
from Myro import*
from random import randint

v=Window("Snake",800,600)
v.setBackground(Color("black"))

listaCuerpo=[]


snake=makePicture("greencircle.png")
snake.x=400
snake.y=300
snake.border=0
listaCuerpo.append(snake)

def cabeza():
    snake=makePicture("greencircle.png")
    snake.border=0
    listaCuerpo.append(snake)    

#cuerpo
'''cuerpo=makePicture("greencircle.png")
cuerpo.x=snake.x-snake.x/2
cuerpo.y=snake.y-snake.y/2
cuerpo.border=0'''

listaComida=[]

#Comida
comida=makePicture("Apple.png")
comida.x=200
comida.y=400
comida.border=0
listaComida.append(comida)

#Texto para los puntos
txtPuntos=Text((700,50),"Puntos:0")
txtPuntos.color=Color("white")

puntosJugador=0

#Bandera de jugando
juegoCorriendo=True

def dibujarBorde():
    global snake
    global x
    global y
    ri=Rectangle((1,1),(10,599))
    ri.draw(v)
    ri.fill=(Color("blue"))
    
    ra=Rectangle((10,1),(790,10))
    ra.draw(v)
    ra.fill=(Color("blue"))
    
    rd=Rectangle((790,1),(799,599))
    rd.draw(v)
    rd.fill=(Color("blue"))
    
    rab=Rectangle((10,590),(790,799))
    rab.draw(v)
    rab.fill=(Color("blue"))
    
    
def atenderTeclado(v,e):
    global snake
    
    if e.key=="Up":
        snake.y-=20
    if e.key=="Down":
        snake.y+=20
    if e.key=="Left":
        snake.x-=20
    if e.key=="Right":
        snake.x+=20
    
    
def dibujarLinea(datos):
    x1=int(datos[1])
    y1=int(datos[2])
    x2=int(datos[3])
    y2=int(datos[4])
    
    linea=Line((x1,y1),(x2,y2))
    if len(datos)>5:
        strColor=datos[5].rstrip("\n")
        linea.color=(Color(strColor))
    linea.draw(v)
    
def interpretar(ent):
    lista=ent.readlines()
    for linea in lista:
        datos=linea.split(" ")
        if datos[0]=="r":
            dibujarRectangulo(datos)
        if datos[0]=="l":
            dibujarLinea(datos)
            
def moverComida():
    global puntosJugador
    ancho=snake.width
    alto=snake.height
    if snake.x>=comida.x-ancho/2 and snake.x<=comida.x+ancho/2:
        if snake.y>=comida.y-alto/2 and snake.y<=comida.y+alto/2:
            comida.x=randint(10,790)
            comida.y=randint(10,590)
            puntosJugador+=10
            txtPuntos.text="Puntos:"+str(puntosJugador)
            cabeza()
            listaCuerpo[1].x=listaCuerpo[0].x-(2*ancho/2)
            listaCuerpo[1].draw(v)

def perderJuego():
    global snake
    if snake.x==790 and snake.y==790:
        txtPierde=Text((400,300),"Game Over")
        txtPierde.color=Color("white")
        txtPierde.draw(v)
        juegoCorriendo=False
        
def moverCuerpo(): 
    for k in range (len(listaCuerpo)):
        listaCuerpo[k].x=listaCuerpo[k-1].x
        
        
def main():
    ent=open("nivelUno.txt","r")
    interpretar(ent)
    ent.close
    comida.draw(v)
    snake.draw(v)
    #Puntos
    txtPuntos.draw(v)
    
    #Bordes
    borde=dibujarBorde()
    
    #Teclado
    onKeyPress(atenderTeclado)
    
    
    while True:
        v.step(0.034)
        if juegoCorriendo:
            moverComida()
            perderJuego()
            moverCuerpo()
v.run(main)