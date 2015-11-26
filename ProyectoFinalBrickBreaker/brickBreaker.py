#encoding: UTF-8
#Sergio Alberto Hernandez Mendez
#Descripcion: Videojuego para proyecto final

from Graphics import *
from Myro import pickOne

#Ventana
nivel = 1
v = Window ("Brick breaker", 800, 600)


#Vidas del usuario y puntos
puntos = 0
vidas = 3

bannerVidasYPuntos = Rectangle((0,0),(800,40))
bannerVidasYPuntos.fill = Color ("cadetblue")
bannerVidasYPuntos.border = 0

txtVidas = Text((50,20),"Vidas: ")
txtVidas.color = Color ("white")
listaVidas = []

txtPuntos = Text((725,20),"Puntos: 0")
txtPuntos.color = Color ("white")

txtPierde= makePicture ("pierde.png")
txtPierde.x = 400
txtPierde.y = 300
txtPierde.border = 0

txtGana= makePicture ("gana.png")
txtGana.x = 400
txtGana.y = 300
txtGana.border = 0

badgeNivel = makePicture ("badge_1.png")

#Puntos maximos
def leerArchivo():
    entrada = open ("puntajes.txt", "r") #Read
    linea = entrada.readline()
    valor = entrada.readline()
    puntos = int(valor)
    entrada.close()
    return puntos

mayor = leerArchivo()
txtAlto = Text ((575, 20), "Marcador mayor: "+ str (mayor))
txtAlto.color = Color ("red")

#Pelota
pelota = makePicture ("pelota.png")
pelota.border = 0
pelota.x = 400
pelota.y = 500


#Paleta
paleta = makePicture ("paleta.png")
paleta.border = 0
paleta.x = 400
paleta.y = 520

#Condiciones pantalla
#Paleta
paletaDentroLadoIzquierdo = paleta.x - paleta.width/2  > 0
paletaDentroLadoDerecho = paleta.x + paleta.width/2  < 800

#Pelota
pelotaDentroLadoIzquierdo = pelota.x - pelota.width/2 > 0
pelotaDentroLadoDerecho = pelota.x + pelota.width/2 < 800
pelotaDentroArriba = pelota.y - pelota.height/2 > 40

#Choque paleta y pelota
choquePaletaPelotaY = pelota.y == 500
choquePaletaPelotaXDer = pelota.x <= paleta.x + paleta.width/2
choquePaletaPelotaXIzq = pelota.x >= paleta.x - paleta.width/2

#Vector direccion e incrementos
incremento = 5
direccion = {"x":-1, "y":-1}

#Variables de juego
juegoCorriendo = True
juegoIniciado = False

#Variables para dibujar mundo
xFila = 80
yFila = 150
listaLadrillos = []
listaLadrillosVidas = []

#Botones para salir y reiniciar
btnSalir = Button ((400,500), "Salir")


def salirJuego(btn,e):
    v.close()
                        
def ponerBotonSalir():
    btnSalir.draw(v)
    btnSalir.connect ("click", salirJuego)

def guardarMarcador():
    anteriores = leerArchivo() # Lee el marcador del archivo
    if puntos > anteriores :     
        salida = open ("puntajes.txt", "w")
        salida.write("Marcador\n")
        salida.write(str (puntos)+"\n")
        salida.close()

def generarVidas():
	for i in listaVidas:
		i.undraw()
	for j in range (vidas):
		x = makePicture ("pelota.png")
		listaVidas.append (x)
		x.x = txtVidas.x + (txtVidas.width+ x.width)/2 + x.width*j + 10
		x.y = txtVidas.y
		x.border = 0
		x.draw(v)

def resetearPelota():
	global direccion, pelota, paleta, juegoIniciado
	paleta.x = 400
	paleta.y = 520

	pelota.x = 400
	pelota.y = 500
	direccion = {"x":-1, "y":-1}
	juegoIniciado = False

def jugadorPierde ():
	guardarMarcador()
	txtPierde.draw(v)
	global juegoCorriendo 
	juegoCorriendo = False
	ponerBotonSalir()

def jugadorGana():
	global juegoCorriendo, btnSalir, fondo
	guardarMarcador()
	juegoCorriendo = False

	txtGana.draw(v)

	ponerBotonSalir()

def nivelTerminado ():
	global vidas, nivel
	vidas += 1
	nivel += 1
	if nivel <= 5:
		pelota.undraw()
		paleta.undraw()
		bannerVidasYPuntos.undraw()
		txtVidas.undraw()
		txtPuntos.undraw()
		txtAlto.undraw()
		for i in listaVidas:
			i.undraw()

		resetearPelota()
		crearMundo()


		paleta.draw(v)
		pelota.draw(v)
		bannerVidasYPuntos.draw(v)
		txtVidas.draw(v)
		txtPuntos.draw(v)
		txtAlto.draw(v)
		for i in listaVidas:
			i.draw(v)
		for j in range (vidas-len(listaVidas)):
			x = makePicture ("pelota.png")
			listaVidas.append (x)
			x.x = txtVidas.x + (txtVidas.width+ x.width)/2 + x.width*(j+len(listaVidas)-1) + 10
			x.y = txtVidas.y
			x.border = 0
			x.draw(v)

	elif nivel > 5:
		jugadorGana()



def comprobarPelotaFuera():
	global vidas
	condicionPelotaFuera = pelota.y - pelota.height/2 >= 600
	if condicionPelotaFuera and vidas > 0:
		vidas -= 1
		resetearPelota()
		listaVidas[vidas].undraw()
		listaVidas.remove(listaVidas[vidas])

	elif vidas == 0:
		jugadorPierde()

def verificarChoqueLadrillos():
	global listaLadrillos, listaLadrillosVidas, direccion, puntos
	indice = 0
	for ladrillo in listaLadrillos:
		condicionChoqueLadrilloArriba = (pelota.y == ladrillo.y - 20) and (pelota.x >= ladrillo.x - ladrillo.width/2) and (pelota.x <= ladrillo.x + ladrillo.width/2) and direccion["y"] == 1 
		condicionChoqueLadrilloLateral = ((pelota.y >= ladrillo.y - ladrillo.height/2) and (pelota.y <= ladrillo.y + ladrillo.height/2)) and ((pelota.x == ladrillo.x - (ladrillo.width + pelota.width)/2) or (pelota.x == ladrillo.x + (ladrillo.width + pelota.width)/2) )
		condicionChoqueLadrilloAbajo = (pelota.y == ladrillo.y + 20) and (pelota.x >= ladrillo.x - ladrillo.width/2) and (pelota.x <= ladrillo.x + ladrillo.width/2) and direccion["y"] == -1
		condicionChoqueEsquinaSI = (pelota.x == ladrillo.x - 50) and (pelota.y == ladrillo.y - 20) and (direccion["x"] > 0 and direccion["y"] > 0)
		condicionChoqueEsquinaSD = (pelota.x == ladrillo.x + 50) and (pelota.y == ladrillo.y - 20) and (direccion["x"] < 0 and direccion["y"] > 0)
		condicionChoqueEsquinaII = (pelota.x == ladrillo.x - 50) and (pelota.y == ladrillo.y + 20) and (direccion["x"] > 0 and direccion["y"] < 0)
		condicionChoqueEsquinaID = (pelota.x == ladrillo.x + 50) and (pelota.y == ladrillo.y + 20) and (direccion["x"] < 0 and direccion["y"] < 0)

		condicionChoqueEsquina = condicionChoqueEsquinaSI or condicionChoqueEsquinaSD or condicionChoqueEsquinaII or condicionChoqueEsquinaID
		#Checar choque ladrillo arriba
		if condicionChoqueLadrilloArriba:
			#Checar vidas de ladrillo
			listaLadrillosVidas [indice] -= 1

			if listaLadrillosVidas [indice] == 2:
				puntos += 50
				color = pickOne(getColorNames())
				while color== "black":
					color = pickOne(getColorNames())
				listaLadrillos[indice].fill = Color (color)

			if listaLadrillosVidas [indice] == 1:
				puntos += 30
				listaLadrillos[indice].border = 0

			if listaLadrillosVidas [indice] == 0 :
				puntos += 20
				listaLadrillos[indice].undraw()
				listaLadrillos.remove (listaLadrillos[indice])
				listaLadrillosVidas.remove (listaLadrillosVidas[indice])
			direccion["y"] *= -1
			break
		if condicionChoqueLadrilloAbajo:
			#Checar vidas de ladrillo
			listaLadrillosVidas [indice] -= 1

			if listaLadrillosVidas [indice] == 2:
				puntos += 50
				color = pickOne(getColorNames())
				while color== "black":
					color = pickOne(getColorNames())
				listaLadrillos[indice].fill = Color (color)

			if listaLadrillosVidas [indice] == 1:
				puntos += 30
				listaLadrillos[indice].border = 0

			if listaLadrillosVidas [indice] == 0 :
				puntos += 20
				listaLadrillos[indice].undraw()
				listaLadrillos.remove (listaLadrillos[indice])
				listaLadrillosVidas.remove (listaLadrillosVidas[indice])
			direccion["y"] *= -1

			break
		#Checar choque lateral
		if condicionChoqueLadrilloLateral or condicionChoqueEsquina:
			#Checar vidas de ladrillo
			direccion["x"] *= -1
			break

		indice +=1

	txtPuntos.text = "Puntos: " + str (puntos)
#'''
def dibujarLadrillo(tipo, numero): 
	global xFila, yFila
	if tipo == "terminoLinea":
		yFila += 20
		xFila = 80

	elif tipo == "vacio":
		xFila += (numero)*80

	else:
		for i in range (numero):
			x = Rectangle ((xFila,yFila),(xFila+80, yFila+20))
			listaLadrillos.append(x)
			x.draw(v)
			
			if tipo == "tipoUno" :
				x.border = 0
				listaLadrillosVidas.append(1)
				color = pickOne(getColorNames())
				while color== "black":
					color = pickOne(getColorNames())
				x.fill = Color (color)

			elif tipo == "tipoDos":
				listaLadrillosVidas.append(2)
				color = pickOne(getColorNames())
				while color == "black":
					color = pickOne(getColorNames())
				x.fill = Color (color)

			elif tipo == "tipoTres":
				listaLadrillosVidas.append(3)
				x.fill = Color("black")

			xFila += 80

def leerNivel (nivel):
	nombreArchivo = "nivel" + "_" + str(nivel)+ ".txt"
	ent = open (nombreArchivo, "r")
	tituloFondo = ent.readline()
	listaMundo = ent.readlines()
	return (tituloFondo, listaMundo)

#Dibuja el mundo obteniendo de un archivo, los ladrillos y items
def crearMundo():
	(archivoFondo, listaMundoEntrada) = leerNivel(nivel)
	global fondo, yFila, badgeNivel
	fondo = makePicture ( archivoFondo.rstrip ("\n") )
	fondo.border = 0
	fondo.draw (v)

	#Poner bloques
	for linea in listaMundoEntrada: #Va linea por linea de bloques
		ladrillos = linea.split(",") #Separa la linea en bloques "tipo numero"
		for ladrillo in ladrillos : #Va por conjunto "tipo numero"
			datos = ladrillo.split() #Separa en {tipo, numero}
			tipo = datos[0]
			numeroLadrillos = int (datos[1])
			dibujarLadrillo(tipo,numeroLadrillos)

		dibujarLadrillo("terminoLinea", 0)
	yFila = 150	
	archivoBadge = "badge_" + str(nivel) + ".png"
	badgeNivel = makePicture (archivoBadge)
	badgeNivel.x = 400
	badgeNivel.y = 300
	badgeNivel.border = 0
	badgeNivel.draw(v)

def verificarChoqueMarcoPaleta():
	global direccion
	if not (pelotaDentroLadoIzquierdo and pelotaDentroLadoDerecho):
		direccion["x"] *= -1
	if not pelotaDentroArriba :
		direccion["y"] *= -1
	if choquePaletaPelotaXIzq and choquePaletaPelotaXDer and choquePaletaPelotaY and (direccion["y"]==1):
		if pelota.x > paleta.x + paleta.width/4 :
			direccion["x"] = 2

		elif pelota.x < paleta.x - paleta.width/4 :
			direccion["x"] = -2

		elif pelota.x <= paleta.x + paleta.width/4 and pelota.x >= paleta.x :
			direccion["x"] = 1

		elif pelota.x >= paleta.x - paleta.width/4 and pelota.x < paleta.x :
			direccion["x"] = -1

		direccion["y"] *= -1

def moverPelota():
	global pelota, pelotaDentroArriba, pelotaDentroLadoIzquierdo, pelotaDentroLadoDerecho, choquePaletaPelotaY, choquePaletaPelotaXDer, choquePaletaPelotaXIzq
	pelota.x += (direccion["x"] * incremento)
	pelota.y += (direccion["y"]* incremento)

	pelotaDentroLadoIzquierdo = pelota.x - pelota.width/2 > 0
	pelotaDentroLadoDerecho = pelota.x + pelota.width/2 < 800
	pelotaDentroArriba = pelota.y - pelota.height/2 > 40

	choquePaletaPelotaY = pelota.y == 500
	choquePaletaPelotaXDer = pelota.x <= paleta.x + paleta.width/2
	choquePaletaPelotaXIzq = pelota.x >= paleta.x - paleta.width/2


def atenderTeclado(v, e):
	global paleta, pelota, juegoIniciado, paletaDentroLadoDerecho, paletaDentroLadoIzquierdo
	paletaDentroLadoDerecho = paleta.x + paleta.width/2 < 800
	paletaDentroLadoIzquierdo = paleta.x - paleta.width/2  > 0

	if e.key == "space" and juegoCorriendo and not juegoIniciado :
		juegoIniciado = True
		badgeNivel.undraw()
		moverPelota() 

	if e.key == "Right" and juegoCorriendo and paletaDentroLadoDerecho:
		paleta.x += 30
		if not juegoIniciado:
			badgeNivel.undraw()
			pelota.x += 30
		

	if e.key == "Left" and juegoCorriendo and paletaDentroLadoIzquierdo:
		paleta.x -= 30
		if not juegoIniciado:
			badgeNivel.undraw()
			pelota.x -= 30 
		
def main():
	crearMundo()

	#Dibujar pelota y paleta
	pelota.draw(v)
	paleta.draw(v)

	#Dibujar letreros
	bannerVidasYPuntos.draw(v)
	txtVidas.draw(v)
	generarVidas()
	txtPuntos.draw(v)
	txtAlto.draw(v)

	onKeyPress(atenderTeclado)

	while True:
		v.step (0.034)
		if juegoCorriendo and juegoIniciado :
			moverPelota()
			verificarChoqueMarcoPaleta()
			verificarChoqueLadrillos()
		comprobarPelotaFuera()
		if len(listaLadrillos) == 0:
			nivelTerminado()

v.run (main)

