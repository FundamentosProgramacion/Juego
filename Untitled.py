#encoding:UTF-8
#Autor:Ernesto Cruz Lopéz
#Proyecto Final

from Graphics import *
from random import randint

def leerArchivo():
    entrada=open("marcador.txt","r")
    linea=entrada.readline()
    valor=entrada.readline()
    valor=valor[0:len(valor)-1]
    puntos=int(valor)
    entrada.close()
    return puntos

txtPuntos=Text((700,50),"Puntos:0")
txtPuntos.color=Color("White")

puntosJugador=0


v=Window("Espacio",800,600)


personaje=makePicture("astro.png")
personaje.y=555
personaje.x=400
personaje.border=0





contador=0
band=True
enemigo=0
enemigoX=0

contadorUno=0
bandUno=True
amigo=0
amigoX=0

contadorDos=0
bandDos=True
blackh=0
blackhX=0

contadorTres=0
bandTres=True
fugaz=0
fugazX=0

listaEnemigos=[]
listaAmigos=[]
listaBlack=[]
listaSFugaz=[]

mayor=leerArchivo()
txtAlto=Text((150,50),"Marcador mayor:"+str(mayor))
txtAlto.color=Color("white")

juegoCorriendo=True


def bTeclado(v,e):

    if e.key =="Left":
        personaje.x-=20
    if e.key=="Right":
        personaje.x+=20
    if personaje.x<=50:
        personaje.x=50
    if personaje.x>=750:
        personaje.x=750

def amigos():
    global contadorUno,bandUno,amigoX
    
    if len(listaEnemigos)>=5:
        if contadorUno>=1 and bandUno == True:
            bandUno=False
            contadorUno=0
            if len(listaAmigos)<100:
                amigo=makePicture("star.png")
                amigo.y=0
                amigo.x=randint(5,750)
                amigo.border=0
                amigo.draw(v)
                listaAmigos.append(amigo)
                amigoX=amigo.x

def moverEstrellas():
    global contadorUno,bandUno,amigo
    y1=570
    y2=570
    
    if contadorUno>=0.001 and bandUno==False:
        bandUno=True
        contadorUno=0
        for k in listaAmigos:
            k.y+=80
            if k.y>590:
                v.undraw(k)
                listaAmigos.remove(k)
            amigo=k.y
            
def blackHoles():
    global contadorDos,bandDos,blackhX, puntosJugador
    
    if puntosJugador>=500:
    
        if contadorDos>=1 and bandDos==True:
            bandDos=False
            contadorDos=0
            if len(listaBlack)<100:
                blackh=makePicture("black.png")
                blackh.y=0
                blackh.x=randint(5,750)
                blackh.border=0
                blackh.draw(v)
                listaBlack.append(blackh)
                blackhX=blackh.y

def moverBlackHole():
    global contadorDos,bandDos,blackh
    y1=570
    y2=570
    
    if contadorDos>=0.001 and bandDos==False:
        bandDos=True
        contadorDos=0
        for b in listaBlack:
            b.y+=120
            if b.y>590:
                v.undraw(b)
                listaBlack.remove(b)
            blackh=b.y

def SFugaz():
    
    global contadorTres,bandTres,fugazX, puntosJugador
    if puntosJugador>=800:
            if contadorTres>=1 and bandTres == True:
                bandTres=False
                contadorTres=0
                if len(listaSFugaz)<100:
                    fugaz=makePicture("Shoot.png")
                    fugaz.y=0
                    fugaz.x=randint(5,750)
                    fugaz.border=0
                    fugaz.draw(v)
                    listaSFugaz.append(fugaz)
                    fugazX=fugaz.x

def moverShootStar():
    global contadorTres,bandTres,fugaz
    y1=570
    y2=570
    
    if contadorTres>=0.001 and bandTres==False:
        bandTres=True
        contadorTres=0
        for s in listaSFugaz:
            s.y+=250
            if s.y>590:
                v.undraw(s)
                listaSFugaz.remove(s)
            fugaz=s.y

def enemigos():

    global contador, band, enemigoX
    if contador>=1 and band == True:
       band = False
       contador=0
       if len(listaEnemigos)<100:
            enemigo = makePicture("aste.png")
            enemigo.y=0
            enemigo.x=randint(5,750)
            enemigo.border=0
            enemigo.draw(v)
            listaEnemigos.append(enemigo)
            enemigoX=enemigo.x
            
def moverAsteroides():
    global contador, band, enemigo
    y1=570
    y2=570
    
    if contador>=0.001 and band==False:
            band=True
            contador=0
            for e in listaEnemigos:
                e.y+=75
                if e.y>=590:
                    v.undraw(e)
                    listaEnemigos.remove(e)
                enemigo = e.y

def colisiones():
    
    a1=0
    s1=0
    b1=0
    c1=0
    
    for e in listaEnemigos:
        if enemigo.x==personaje.x:
            a1=1
            v.undraw(e)
            listaEnemigo.remove(e)
    
    for k in listaAmigos:
        if amigo.x==personaje.x:
            s1=1
            v.undraw(k)
            listaEnemigo.remove(k)
    
    for b in listaBlack:
        if blackh.x==personaje.x:
            b1=1
            v.undraw(b)
            listaBlack.remove(b)
    
    for s in listaSFugaz:
        if fugaz.x==personaje.x:
            c1=1
            v.undraw(s)
            listaSFugaz.remove(k)

def sumaPuntos():
    global puntosJugador, juegoCorriendo
    for k in listaAmigos:
        ancho = k.width
        alto = k.height
        if personaje.x>=k.x - ancho/2 and personaje.x<= k.x+ancho/2:
                if personaje.y>=k.y - alto/2 and personaje.y<=k.y+alto/2:

                    puntosJugador += 50
                    txtPuntos.text = "Puntos: " + str(puntosJugador)
                    k.undraw()
                    listaAmigos.remove(k)
                    
                    if puntosJugador>=1000:
                        txtGana = Text ((400,300),"WIN")
                        txtGana.color = Color("White")
                        txtGana.draw(v)
                        juegoCorriendo = False
                        guardarMarcador()
                        ponerBotonSalir()
                       

def restaPuntos():
    global puntosJugador, juegoCorriendo
    for e in listaEnemigos:
        ancho = e.width
        alto = e.height
        if personaje.x>=e.x - ancho/2 and personaje.x<= e.x+ancho/2:
                if personaje.y>=e.y - alto/2 and personaje.y<=e.y+alto/2:

                    puntosJugador -= 20
                    txtPuntos.text = "Puntos: " + str(puntosJugador)
                    e.undraw()
                    listaEnemigos.remove(e)
                    
                    if puntosJugador<=-150:
                        txtPierde = Text ((400,300),"Game Over")
                        txtPierde.color = Color("White")
                        txtPierde.draw(v)
                        juegoCorriendo = False
                        guardarMarcador()
                        ponerBotonSalir()
                        ponerBotonReiniciar()

def looser():

    global juegoCorriendo
    for b in listaBlack:
        ancho = b.width
        alto = b.height
        if personaje.x >=b.x-ancho/2 and personaje.x<=b.x+ancho/2:
            if personaje.y>=b.y-ancho/2 and personaje.y<=b.y+ancho/2:
               
                txtPierde = Text ((400,300),"Game Over")
                txtPierde.color = Color("White")
                txtPierde.draw(v)
                juegoCorriendo = False
                guardarMarcador()
                ponerBotonSalir()



def cartel():
    global puntosJugador
    if puntosJugador<=0: 
        txtMove = Text ((400,590),"Ocupa las flechas izquierda y derecha para movimiento")
        txtMove.color = Color("White")  
        txtMove.draw(v)
        txtStar = Text ((400,10),"Toma todas las estrellas que puedas, busca las cometas y esquiva los demás objetos")
        txtStar.color = Color("White")
        txtStar.draw(v)
                        

def champion():

    global juegoCorriendo
    for s in listaSFugaz:
        ancho = s.width
        alto = s.height
        if personaje.x >=s.x-ancho/2 and personaje.x<=s.x+ancho/2:
            if personaje.y>=s.y-ancho/2 and personaje.y<=s.y+ancho/2:
               
                txtGana = Text ((400,300),"WIN")
                txtGana.color = Color("White")
                txtGana.draw(v)
                juegoCorriendo = False
                guardarMarcador()
                ponerBotonSalir()
             
                                
def salirJuego(btn,e):
    v.close()


def ponerBotonSalir() :
    btnSalir = Button((400,150),"S a l i r")
    btnSalir.draw(v)
    btnSalir.connect("click",salirJuego)
     
                
def guardarMarcador():
    anteriores = leerArchivo()
    if puntosJugador > anteriores :
        salida = open("marcador.txt","w")
        salida.write("marcador\n")
        salida.write(str(puntosJugador) + "\n")
        salida.close()
        
def main():
    
    global contador,contadorUno,contadorDos,contadorTres
    
    fondo=makePicture("espacio.jpg")
    fondo.draw(v)
    piso=Rectangle((0,595),(800,600))
    piso.color=(Color("Orange"))
    piso.bodyType="static"
    piso.draw(v)
    
    personaje.draw(v)
    
    txtPuntos.draw(v)
    
    onKeyPress(bTeclado)
    
    tiempo=0
    LIMITE=1
    
    while True:
        v.step(0.034)
        if juegoCorriendo:
           tiempo+=0.034
           if tiempo>=LIMITE:
                tiempo=0
                LIMITE-=.01
                
                enemigos()
                moverAsteroides()
                
                SFugaz()
                moverShootStar()
                
                blackHoles()
                moverBlackHole()
          
                amigos()
                moverEstrellas()
                
                
                cartel()
           
           contador+=.034
           contadorUno+=.078
           contadorDos+=.025
           contadorTres+=.01
           sumaPuntos()
           restaPuntos()
           looser()
           champion()
    
v.run(main)