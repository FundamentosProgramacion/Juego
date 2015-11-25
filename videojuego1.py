#Encoding:UTF-8
#Autor:Manuel Zavala
#Videojuego

from Graphics import *
from random import randint
from Myro import *

#Crear la ventana gráfica
fondo=makePicture("dragonball.jpg")
ven=Window("Dragon Ball Z el juego", 600,300)
fondo.draw(ven)
titulo=Text((300,50),"Dragon Ball Z!")
titulo.fill=Color("white")
titulo.fontSize=45
titulo.draw(ven)

#Botones del menú
iniciar=Button(Point(250,200),"Iniciar")
iniciar.draw(ven)
puntuacion=Button(Point(300,190)," Puntuación \n    anterior")
puntuacion.draw(ven)
play("dragonball.wav")

#Funcion Abrir ventana
def abrirven(o,e):
    fondo=makePicture("fondo.jpg")
    ven=Window("Puntuación", fondo.width, fondo.height)
    fondo.draw(ven)
    entrada=open("puntuacion.txt","r")
    a=entrada.readline()
    x=fondo.x
    texto=Text((x,30),"La puntuación anterior fue:"+ a)
    texto.fontSize=20
    texto.fill=Color("white")
    texto.draw(ven)

puntuacion.connect("click", abrirven)

x=1000

def empezarJuego(obj,evento):
    global x
    x=0
    ven.close()
    
iniciar.connect("click",empezarJuego)

while x>=1000:
    wait(1)

wait(x)

#Ventana del videojuego
v = Window("Dragon Ball Z!",550,700)
v.mode="physics"
a = makePicture("fondo.jpg")
b = makePicture("fondo.jpg")
b.x = -550/2
a.draw(v)
b.draw(v)
play("theme.wav")

#lista de esferas
esferas=[]

contar=0 #cuenta las esferas caida
sumar=0  #suma de puntos

#Gokú
goku=makePicture("alien.png")
goku.x=150
goku.y=600
goku.border=0
goku.draw(v)

#Mueve a Gokú de izquierda a derecha
def atenderBase(b,evento):
    tecla=evento.key
    if tecla=='Left':
        goku.x-=5
        
    if tecla=='Right':
        goku.x+=5
            
def main():
    global contar,sumar
   
    #textos de instrucciones, puntuacion y bloques caidos
    nose=Text((450,69),"Ayuda a Gokú a atrapar las esferas del dragón")
    nose.bodyType="static"
    nose.draw(v)
    nose.fill=Color("white")
        
    ins=Text((250,15),"Mueve a Gokú con derecha e izquierda")
    ins.draw(v)
    ins.bodyType="static"
    ins.fill=Color("white")
    
    puntos=Text((500,10),"Puntos")
    puntos.bodyType="static"
    puntos.fill=Color("white")
    puntos.draw(v)
    
    caidos=Text((500,30),"Caidos")
    caidos.bodyType="static"
    caidos.fill=Color("white")
    caidos.draw(v)
    
    onKeyPress(atenderBase)

    #circulo que deja caer las esferas
    c=Circle((70,70),30)
    c.bodyType="static"
    c.fill=None
    c.border=0
    c.draw(v)
    
    INCREMENTO_X=+3
    
    while v.isRealized():
        v.step(0.023)
        
        #movimiento del fondo
        a.x = a.x+2
        b.x = b.x+2
        if b.x>275+550:
            b.x = -276
        if a.x>275+550 :
            a.x = -273
          
        #movimiento del círculo
        c.x+= INCREMENTO_X
        if c.x>=545 or c.x<=5:
            INCREMENTO_X=-INCREMENTO_X
        
        #creacion de las esferas
        na=randint(1,150)
        if na<=10:
            r=Circle((70,70),30)          
            r.fill=Color("orange")
            r.border=0
            r.x=c.x
            r.y=c.y
            r.bounce=0.0
            r.friction=0
            v.draw(r)
            esferas.append(r)
                    
        #Revisa si la esfera no fue atrapada y la cuenta
        for r in esferas:
            
             #elimina la esfera y cuenta puntos 
            if r.y>700:
                r.undraw()
                esferas.remove(r)
                contar+=1
                caidos.text="Caidos:" + str(contar)
             
                #condición para que elimine las esferas y sume puntos   
            if (r.x==goku.x or(r.x>=goku.x-50 and r.x<=goku.x+50) )and (r.y==goku.y or(r.y>goku.y-50 and r.y<=goku.y+50)):
                sumar+=5
                puntos.text="Puntos: " + str(sumar)
                play("grito.wav")
                r.undraw()
                r.x=0
                r.y=0

                
        if contar==5:#Game over
            fin=Text((250,350),"Game Over")
            fin.fill=Color("red")
            fin.fontSize=50
            fin.draw(v)
            break
            
    #Guarda el puntaje
    salida=open("puntuacion.txt","w")
    salida.write(str(sumar))
    salida.close()
main()