#encoding: utf-8
#Autor: Brian Saggiante A01377511
#Proyecto Final Videojuego

from Graphics import*
from random import randint


v=Window('Bruce Lee',800,600)
fondo=makePicture('japan.jpg')
fondo.draw(v)
v.mode='physics'
v.setBackground(Color('white'))
v.gravity=Vector(0,25)


bruce=makePicture('brucelee.png')
bruce.x=750
bruce.bounce=0
bruce.border=0

tryHard=makePicture('Bruce.jpg')
tryHard.bodyType='static'
txtTryHard=Text((700,200),'TRY HARD')
txtTryHard.bodyType='static'
txtTryHard.color=Color('red')

deadpool=makePicture('deadpool.png')
deadpool.x=400
deadpool.y=500
deadpool.bodyType='static'
deadpool.border=0
deadpool.draw(v)

enemigo=makePicture('enemigo.png')
enemigo.x=100
enemigo.bounce=0
enemigo.border=0

enemigo2=makePicture('leono.png')
enemigo2.border=0
enemigo2.bounce=0
enemigo2.x=400


nivelJuego=1
nivel=nivelJuego+1
txtNivel=Text((700,50),'Nivel: 1')
txtNivel.bodyType='static'
txtNivel.color=Color('cyan')
txtNivel.draw(v)

def atenderTeclado(v,e):
    if e.key=='space':
        bruce.y-=50
    if e.key=='Right':
        bruce.x+=20
    if e.key=='Left':
        bruce.x-=20
    if e.key=='Up':
        bruce.rotation=bruce.rotation+45
    if e.key=='Down':
        bruce.rotation=bruce.rotation-45
        


def detectaColision():
    ancho=bruce.width
    alto=bruce.height
    if bruce.x+ancho*2>=enemigo.x+ancho and bruce.x+ancho<=enemigo.x+ancho*2:    
        enemigo.undraw()
        txtNivel.text='Nivel: ' +str(nivel)
        txtNivel.color=Color('cyan')
        txtNivel.bodyType='static'
        txtNivel.draw(v)
    if bruce.x+alto*2>=enemigo2.x+alto and bruce.x+alto<=enemigo2.x+alto*2:
        enemigo2.undraw()
        
           
      
def salirJuego(btn,e):
    if btnSalir.connect:
        v.close()
        
    
btnSalir=Button((700,100),'Salir')     

def main():
   
    
    piso=Rectangle((0,590),(800,599))
    piso.bodyType='static'
    piso.color=None
    piso.bounce=0
    piso.draw(v)
    
    pared=Rectangle((0,2),(10,590))
    pared.bodyType='static'
    pared.bounce=1
    pared.color=None
    pared.draw(v)
    
    pared2=Rectangle((790,2),(800,590))
    pared2.bodyType='static'
    pared2.bounce=1
    pared2.color=None
    pared2.draw(v)
    
    techo=Rectangle((10,1),(799,10))
    techo.bodyType='static'
    techo.bounce=0
    techo.color=None
    techo.draw(v)

    bruce.draw(v)
    enemigo.draw(v)
    enemigo2.draw(v)
    
    onKeyPress(atenderTeclado)
    
    juegoCorriendo=True
    tiempo=0
    LIMITE=1
    while juegoCorriendo==True:
        v.step(0.01)
        detectaColision()
        if bruce.y<0:
            txtPierde=Text((700,300),'GAME OVER')
            txtPierde.color=Color('red')
            txtPierde.draw(v) 
            juegoCorriendo=False
            fondo.undraw()
            tryHard.draw(v)
            txtTryHard.draw(v)  
            btnSalir.connect('click',salirJuego)
            btnSalir.draw(v)
            txtNivel.undraw()
        ancho=bruce.width
        alto=bruce.height
        if bruce.x+ancho*3>=deadpool.x+ancho and bruce.x+ancho<=deadpool.x+ancho*3:
            if bruce.y+ancho*3>=deadpool.y+ancho and bruce.y+ancho<=deadpool.y+ancho*3:
                fondo.undraw()
                tryHard.draw(v)
                txtTryHard.draw(v)  
                btnSalir.connect('click',salirJuego)
                btnSalir.draw(v)
                txtNivel.undraw()
                bruce.undraw()
                
            
            
      

v.run(main)