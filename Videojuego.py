#encoding:UTF-8
#Jorge Daniel Jurez Ruiz
#Proyecto Final

from Graphics import*
from random import*
import Myro

v=Window("Viajando por el mundo",800,600)
juegoCorriendo=False
pato=makePicture("Pato 1.png")
pato.border=0
puntos=0
reloj=60
txtTiempo=Text((100,50), "Tiempo 60")
txtPuntos=Text((700,50), "Puntos:0")
txtHS=Text((400,75),"HIGH SCORE:0")
nivel=1
p=20

listaObjetos=[]
listaBombas=[]
listaRegs=[]

pantalla=Rectangle((100,200),(700,400))
txtEsc=Text((400,220),"Escoge la tu personaje favorito")
pantalla.color=Color("white")
txtEsc.color=Color("black")
pato1=makePicture("pato 1.png")
pato1.x=200
pato1.y=300
pato1.border=0
pato2=makePicture("pato 2.png")
pato2.x=400
pato2.y=300
pato2.border=0
pato3=makePicture("pato 3.png")
pato3.x=600
pato3.y=300
pato3.border=0
btnRocky=Button((175,350), "Rocky" )
btnHenry=Button((375,350), "Henry" )
btnSpicy=Button((575,350), "Spicy" )

def reiniciarJuego(btn,e):
    main()
    
def salirVentana(btn,e):
    v.close()

def escogerPersonaje():
    global pato1, pato2, pato3, pantalla
    global btnRocky, btnHenry, btnSpicy
    btnRocky.connect("click", atenderBoton)
    btnHenry.connect("click", atenderBoton)
    btnSpicy.connect("click", atenderBoton)
    pantalla.draw(v)
    txtEsc.draw(v)
    pato1.draw(v)
    pato2.draw(v)
    pato3.draw(v)
    btnRocky.draw(v)
    btnHenry.draw(v)
    btnSpicy.draw(v)
    
    

def atenderBoton(btn,e):
    global pato1, pato2, pato3, pantalla, juegoCorriendo
    global btnRocky, btnHenry, btnSpicy, pato, txtEsc, p
    if btn.Label=="Rocky":
        pato=pato1        
    if btn.Label=="Henry":
        pato=pato2        
    if btn.Label=="Spicy":
        pato=pato3        
    pato1.undraw()
    pato2.undraw()
    pato3.undraw()
    pantalla.undraw()
    txtEsc.undraw()
    btnRocky.Hide()
    btnHenry.Hide()
    btnSpicy.Hide()
    juegoCorriendo=True
    pato.x=300
    pato.y=400
    pato.draw(v)
    


def crearBombas():
    bomba=makePicture("bomba.png")
    bomba.border=0
    bomba.y= 0
    bomba.x=randint(bomba.width,800-bomba.width)
    bomba.draw(v)
    listaBombas.append(bomba)
    
def moverBombas():
    for bomba in listaBombas:
        bomba.y+=10 
        if bomba.y>600+bomba.height:
            listaBombas.remove(bomba)
            bomba.undraw()
    
def verificarChoqueBomba():
    global juegoCorriendo
    global puntos
    for b in listaBombas:
        ancho=b.width
        alto=b.height
        if pato.x>=b.x-ancho/2 and pato.x<=b.x+ancho/2:
            if pato.y>=b.y-alto/2 and pato.y<=b.y+alto/2:
                puntos-=1
                listaBombas.remove(b)
                b.undraw()
                sound =Myro.makeSound("Punch_-_Sound_Effect.wav") 
                Myro.play("Punch_-_Sound_Effect.wav")

def crearObjetos1(obj):
    obj.border=0
    obj.x=randint(0+obj.width,800-obj.width)
    obj.y=randint(0+obj.height,600-obj.height)
    obj.draw(v)
    listaObjetos.append(obj)
    
def crearObjetos(obj):
    obj.border=0
    obj.x= 800+obj.width
    obj.y=randint(obj.height,600-obj.height)
    obj.draw(v)
    listaObjetos.append(obj)
    
def verificarChoqueObjeto():
    global juegoCorriendo
    global puntos
    for b in listaObjetos:
        ancho=b.width
        alto=b.height
        if pato.x>=b.x-ancho/2 and pato.x<=b.x+ancho/2:
            if pato.y>=b.y-alto/2 and pato.y<=b.y+alto/2:
                puntos+=1
                listaObjetos.remove(b)
                b.undraw()
                sound =Myro.makeSound("You_win_sound_effect_1.wav") 
                Myro.play("You_win_sound_effect_1.wav")
        
def moverLento():
    for c in listaObjetos:
        c.x-=10
 
                    
def moverRapido():
    for c in listaObjetos:
        c.x-=15
        
    
 
def crearRegresos():
    reg=makePicture("reg.png")
    reg.border=0
    reg.x= 800+reg.width
    reg.y=randint(reg.height,600-reg.height)
    reg.draw(v)
    listaRegs.append(reg)

def moverRegs():
    for c in listaRegs:
        if nivel==4:
            c.x-=10
        if nivel==5:
            c.x-=20
        
def verificarChoqueReg():
    global juegoCorriendo, reloj
    for b in listaRegs:
        ancho=b.width
        alto=b.height
        if pato.x>=b.x-ancho/2 and pato.x<=b.x+ancho/2:
            if pato.y>=b.y-alto/2 and pato.y<=b.y+alto/2:
                reloj-=5
                listaRegs.remove(b)
                b.undraw()
                sound =Myro.makeSound("Punch_-_Sound_Effect.wav") 
                Myro.play("Punch_-_Sound_Effect.wav")



def atenderTeclado(btn,e):
    if e.key=="Up":
        pato.y-=20
    if e.key=="Down":
        pato.y+=20
    if e.key=="Left":
        pato.x-=20
    if e.key=="Right":
        pato.x+=20

def main():
    fondo5=makePicture("Nivel 5.jpg")
    fondo5.border=0
    fondo5.draw(v)    
    fondo4=makePicture("Nivel 4.jpg")
    fondo4.border=0
    fondo4.draw(v)
    fondo3=makePicture("Nivel 2.jpg")
    fondo3.border=0
    fondo3.draw(v)    
    fondo2=makePicture("Nivel 3.jpg")
    fondo2.border=0
    fondo2.draw(v)
    fondo1=makePicture("Nivel 1.jpg")
    fondo1.border=0
    fondo1.draw(v)
    global fondo1, fondo2, fondo3, fondo4
    fTiempo=RoundedRectangle((50, 35), (150, 60), 10)
    fTiempo.fill=Color("black")
    fTiempo.draw(v)
    txtTiempo.color=Color("white")
    txtTiempo.draw(v)
    fPuntos=RoundedRectangle((650, 35), (750, 65), 10)
    fPuntos.fill=Color("black")
    fPuntos.draw(v)
    txtPuntos.color=Color("white")
    txtPuntos.draw(v)
    escogerPersonaje()
    
    onKeyPress(atenderTeclado)
    global reloj
    tiempo=0
    tiempo2=0
    limite=1
    limite2=3
    

    while True:
        v.step(0.034)
        global juegoCorriendo
        global nivel, listaObjetos
        global puntos, highS, txtHS, p
        
        if juegoCorriendo:
            tiempo+=0.05
            if tiempo>=limite:
                tiempo=0
                reloj-=1
                txtTiempo.text="Tiempo "+str(reloj)
                txtPuntos.text="Puntos:"+str(puntos)
                if reloj<=0: 
                    juegoCorriendo=False                                       
                    perder=makePicture("Roasted.jpg")                    
                    txtPerder=Text((400,50),"GAME OVER")
                    txtPerder.color=Color("white")
                    perder.draw(v)
                    txtPerder.draw(v)                    
                    sound =Myro.makeSound("Wrong_Buzzer_-_Sound_Effect.wav") 
                    Myro.play("Wrong_Buzzer_-_Sound_Effect.wav")
                    highS=((nivel-1)*20)+puntos
                    entrada=open("highScore.txt","r")
                    cadena=entrada.read()
                    if highS>int(cadena):     
                        salida=open("highScore.txt","w")
                        salida.write(str(highS))
                        salida.close()
                        txtHS.text="HIGH SCORE:"+str(highS)
                        txtHS.color=Color("white")
                        txtHS.draw(v)
                    else:
                        print(cadena)
                        txtHS.text="HIGH SCORE:"+ str(cadena)
                        txtHS.color=Color("white")
                        txtHS.draw(v)
                    entrada.close()
                    btnSalir=Button((400,550), "Salir" )
                    btnSalir.draw(v)
                    btnSalir.connect("click",salirVentana )

                    
                if nivel==1:
                    obj=makePicture("barco.png")
                    crearObjetos1(obj)
                    crearBombas()                            
                    if puntos>=p:
                        nivel+=1
                        reloj=60
                        puntos=0
                        fondo1.undraw()                                                           
                        for b in listaObjetos:
                            b.undraw()
                        listaObjetos=[]
                if nivel==2:
                    obj=makePicture("congo.png")
                    crearObjetos(obj)
                    crearBombas()
                    if puntos>=p:
                        nivel+=1
                        reloj=60
                        puntos=0
                        fondo2.undraw()
                        for b in listaObjetos:
                            b.undraw()
                        listaObjetos=[]
                if nivel==3:
                    obj=makePicture("queso.png")
                    crearObjetos(obj)
                    crearBombas()
                    if puntos>=p:
                        nivel+=1
                        reloj=60
                        puntos=0
                        fondo3.undraw()
                        for b in listaObjetos:
                            b.undraw()
                        listaObjetos=[]
                if nivel==4:
                    obj=makePicture("koo.png")
                    crearObjetos(obj)
                    crearBombas()
                    if puntos>=p:
                        nivel+=1
                        reloj=60
                        puntos=0
                        fondo4.undraw()
                        for b in listaObjetos:
                            b.undraw()
                        listaObjetos=[]
                if nivel==5:
                    obj=makePicture("sushi.png")
                    crearObjetos(obj)
                    crearBombas()
                    crearRegresos()
                    if puntos>=p:
                        juegoCorriendo=False
                        a=makePicture("winner.png")
                        a.draw(v)
                        fondo5.undraw()
                        sound =Myro.makeSound("Sonic_Unleashed_Soundtrack_-_Clear_Fanfare_2.wav") 
                        Myro.play("Sonic_Unleashed_Soundtrack_-_Clear_Fanfare_2.wav")
                        highS=100
                        txtHS=Text((400,75),"HIGH SCORE:"+ str(highS))
                        txtHS.color=Color("white")
                        txtHS.draw(v)
                        btnSalir=Button((400,550), "Salir" )
                        btnSalir.draw(v)
                        btnSalir.connect("click",salirVentana )
                        
                        
            if nivel==4:
                tiempo2+=0.05            
                if tiempo2>=limite2:
                    tiempo2=0
                    crearRegresos()
                        
            if nivel==1:
                moverBombas()
                verificarChoqueObjeto()
                verificarChoqueBomba()
                   
            if nivel==2:
               moverLento()
               moverBombas()
               verificarChoqueObjeto()
               verificarChoqueBomba()
           
            if nivel==3:
                moverRapido()
                moverBombas()
                verificarChoqueObjeto()
                verificarChoqueBomba()
                
            if nivel==4:
                moverRapido()
                moverBombas()
                moverRegs()
                verificarChoqueObjeto()
                verificarChoqueBomba()
                verificarChoqueReg()
                
            if nivel==5:
                moverRapido()
                moverBombas()
                moverRegs()
                verificarChoqueObjeto()
                verificarChoqueBomba()
                verificarChoqueReg()

main()