#!/usr/bin/python
# -*- coding: utf-8 -*-

#######################################################################
#
# ORT - Facultad de Ingenieria
# Sistemas Embebidos 2018 - Obligatorio 2
#
# archivo: codigo.py 
# version: v41
#
# Integrantes: Eduardo Thevenet - Nro: 168626
#              Federico Silva - Nro: 189494
#              Gonzalo Becerra - Nro: 184509
#
######################################################################



# ----------  Se incluyen librebrias  ------------------------------
import datetime
import mail  # Se importa la libreria creada para enviar emails mail.py
import serial
import csv
import os
import shutil
import RPi.GPIO as GPIO
import mysql.connector


# -----------  Se configuran perifericos y de definen variables ------
suma = 0

GPIO.setmode(GPIO.BCM) # Se utiliza la configuracion BCM del GPIO para identificar los puertos
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Boton aceptar se configura como IN con un pullup interno
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Boton cancelar se configura con IN con un pullup interno 
GPIO.setup(25, GPIO.IN) #Switch de modo se configura com IN
GPIO.input(25)

pathNroTransaccion = "/var/www/html/NroTransaccion.csv"
pathTempTransaccion = "/var/www/html/TempTransaccion.csv"
pathEstadoSistema = "/var/www/html/estado.txt"
pathConfig = "/var/www/html/config.csv"
pathCodME = "/var/www/html/codME.csv"

with open(pathConfig, 'r') as csv_file:
	reader = csv.reader(csv_file)
	for row in reader:
		host = row[0]
		user = row[1]
		password = row[2]
		database = row[3]
		port = row[4]

mibase = mysql.connector.connect(
	host=host,
	user=user,
	password=password,
	database=database,
	port=port
)
micursor = mibase.cursor()


# ---------------- Funciones ------------------------

def activaGPIO():

	GPIO.add_event_detect(23, GPIO.FALLING, interrupcionAceptar, bouncetime=300)
	GPIO.add_event_detect(24, GPIO.FALLING, interrupcionCancelar, bouncetime=300)


def desactivaGPIO():
	
	GPIO.remove_event_detect(23)
	GPIO.remove_event_detect(24)


def interrupcionAceptar(canal): # Callback de interrupcion del boton ACEPTAR
	global flagAceptar
	flagAceptar = True


def interrupcionCancelar(canal): # Callback del interrupion del boton CANCELAR
	global flagCancelar
	flagCancelar = True

def eventos(msj):
	sql = "INSERT INTO errorlog (id_transacc, descripcion) VALUES (%s,%s)"
	val = (str(nroTransaccion), str(msj))
	micursor.execute(sql,val)
	mibase.commit()

def aceptar():
	
	if hayStock() and hayArticulo():
		actualizaStock(-1)
		if stockSuficiente:
			print("Transaccion confirmada")
			eventos("Transaccion confirmada")
			incrementaNroTransaccion()
		resetTempTransaccion()
		resetCodME()
		global suma
		suma = 0
	
	else:
		print("Transaccion invalida")
		eventos("Transaccion invalida")
		resetTempTransaccion()
		resetCodME()
		global suma
		suma = 0
	
	global flagAceptar 
	flagAceptar = False


def cancelar():
	
	print("Transaccion reseteada")
	eventos("Transaccion reseteada")
	resetTempTransaccion()
	resetCodME()
	global suma
	suma = 0
	global flagCancelar 
	flagCancelar = False


def modoNormal(): 
	
	global suma

	leeCodigo()
	while (codigo == ""  and not flagCancelar and not flagAceptar):
		leeCodigo()

	if (not flagCancelar and not flagAceptar):
		if existeArticulo():
			m1="El articulo de codigo: " + str(codigo) + " tiene descripcion: "+descripcionBuscada+" y precio: "+str(precioBuscado)
			print(m1)
			eventos(m1)
			suma = int(suma) + int(precioBuscado)
			m2="El total acumulado es de: "+str(suma)
			print(m2)
			eventos(m2)
			tempTransaccion(suma) 
		else:
			sql = "INSERT INTO errorlog (id_transacc, descripcion) VALUES (%s,%s)"
			m = 'Se escaneo el codigo: '+str(codigo)+' que no existe en el stock.'
			val = (str(nroTransaccion), str(m))
			micursor.execute(sql,val)
			mibase.commit()


def modoEspecial():

	leeCodigo()
	while (codigo == "" and not flagCancelar and not flagAceptar):
		leeCodigo()

	if (not flagCancelar and not flagAceptar):
		if existeArticulo():
			actualizaStock(1)

			fileWriter = open(pathCodME, 'w')
			writer = csv.writer(fileWriter)
			m= "Se ha incrementado el stock del producto: "
			writer.writerow(["1",m,codigo])
			fileWriter.close()

			m1="Se ha incrementado el stock del producto: "+codigo
			eventos(m1)

		else:
			fileWriter = open(pathCodME, 'w')
			writer = csv.writer(fileWriter)
			p = "Codigo no encontrado, ingrese la siguiente informacion: "
			writer.writerow(["2",p,codigo])
			fileWriter.close()

			sql = "INSERT INTO errorlog (id_transacc, descripcion) VALUES (%s,%s)"
			m = 'Se escaneo el codigo: '+str(codigo)+' que no existe en el stock.'
			val = (str(nroTransaccion), str(m))
			micursor.execute(sql,val)
			mibase.commit()


def hayArticulo(): # SI EL TEMPORAL DE TRANSACCIONES SE ENCUENTRA VACIO NO SE HABILITARA EL BOTON ACEPTAR
	bandera = False

	if os.path.isfile(pathTempTransaccion):
		with open(pathTempTransaccion, 'r') as csv_file:
			reader = csv.reader(csv_file)
			for fila in reader:
				dato = fila[0]
				if dato != "":
					bandera = True

		return bandera


def hayStock(): #SI CODIGO ESCANEADO TIENE STOCK 0 NO SE AGREGA A LA TRANSACCION

	bandera = True

	sql = "SELECT * FROM productos WHERE id_producto = %s"

	micursor.execute(sql, (str(idBuscado),))
	myresult = micursor.fetchall()

	if myresult == []:
		m="Codigo no encontrado"
		print (m)
		eventos(m)
	else:
		lista = list (myresult[0])
		if int(lista[4]) == 0:
			bandera = False

	return bandera


def leeCodigo(): #LEE EL CODIGO ESCANEADO
	
	global codigo
	global ser

	codigo = ser.readline()


def tempTransaccion(sumaAcumulada): #GUARDA LOS CODIGOS ESCANEADOS DURANTE CADA TRANSACCION
	
	fileWriter = open(pathTempTransaccion, 'a+')
	writer = csv.writer(fileWriter)
	writer.writerow([idBuscado, codigo, descripcionBuscada, precioBuscado, sumaAcumulada])
	fileWriter.close()


def resetTempTransaccion(): #RESETEA EL ARCHIVO TempTransaccion.csv
	
	fileReader = open(pathTempTransaccion, 'w')
	fileReader.close()

def resetCodME(): #RESETEA EL ARCHIVO TempTransaccion.csv
	
	fileWriter = open(pathCodME, 'w')
	writer = csv.writer(fileWriter)
	writer.writerow(["0","Escanee producto"])
	fileWriter.close()
	eventos ("Escanee producto")


def agregaArticulo(unaDescripcion, unPrecio, unUmbral): #AGREGA EL ARTICULO AL ARCHIVO DE STOCK.
	
	sql = "INSERT INTO productos (codigo, descripcion, precio, cantidad, umbral) VALUES (%s,%s,%s,%s,%s)"
	val = (str(codigo),unaDescripcion, int(unPrecio), 1, int(unUmbral))
	micursor.execute(sql,val)

	mibase.commit()
	m="Se agrego el articulo al stock"
	print (m)
	eventos(m)


def existeArticulo(): #BUSCA EL ARTICULO POR CODIGO

	global idBuscado
	global descripcionBuscada
	global precioBuscado
	global stockBuscado
	global umbralBuscado

	bandera = False

	sql = "SELECT * FROM productos WHERE codigo = %s"

	micursor.execute(sql, (str(codigo),))
	myresult = micursor.fetchall()

	if myresult == []:
		m="El articulo no se encuentra en stock"
		print(m)
		eventos(m)
	else:
		bandera = True
		lista = list (myresult[0])

		idBuscado = lista[0]
		descripcionBuscada = lista[2]
		precioBuscado = lista[3]
		stockBuscado = lista[4]
		umbralBuscado = lista[5]

	return bandera


def actualizaStock(valor): #MODIFICA EL STOCK DEL ARTICULO.

	global stockSuficiente
	stockSuficiente = True
	identificador = 0
	alarma = False

	if (valor == -1):
		with open(pathTempTransaccion, 'r') as csv_file:
			reader = csv.reader(csv_file)
			for row in reader:
				identificador = row[0]
			
				sql = "SELECT * FROM productos WHERE id_producto = %s"
				micursor.execute(sql, (str(identificador),))
				myresult = micursor.fetchall()
				if myresult == []:
					print "Codigo no encontrado"
				else:
					listaA = list (myresult[0])
					if int(listaA[4]) == 0:
						sql = "INSERT INTO errorlog (id_transacc, descripcion) VALUES (%s,%s)"
						m = 'Se escaneo el codigo: '+str(codigo)+' cuyo stock es 0'
						val = (str(nroTransaccion), str(m))
						micursor.execute(sql,val)
						mibase.commit()
						print 'Transanccion invalida por stock insuficiente'
						stockSuficiente = False
					else:
						m2="Se decremento el stock del producto: "+str(codigo)
						modificaStock(identificador,-1,m2)

						eventos(m2)

						sql = "INSERT INTO transacclog (id_transacc, id_producto) VALUES (%s,%s)"
						val = (str(nroTransaccion), str(identificador))
						micursor.execute(sql,val)
						mibase.commit()

						sql = "SELECT * FROM productos WHERE id_producto = %s"
						micursor.execute(sql, (str(identificador),))
						myresult = micursor.fetchall()
						if myresult == []:
							m3="El articulo no se encuentra en stock"
							print(m3)
							eventos(m3)
						else:
							listaB = list (myresult[0])
							cod = listaB[1]
							cant = listaB[4]
							umbral = listaB[5]

							if cant <= umbral:
								alarma = True
			if alarma:
				m4="Se esta agotando el articulo de codigo: "+cod
				print(m4)
				eventos(m4)

				sql = "SELECT * FROM variables"

				micursor.execute(sql)
				myresult = micursor.fetchall()

				if myresult == []:
					m5="Configurar variables para alerta por falta de stock"
					print(m5)
					eventos(m5)

				else:
					listaC = list (myresult[0])
					correo = listaC[1]
					asunto = listaC[2]
					mensaje = listaC[3]

				mail.enviar(correo,asunto,mensaje,cod)

	if (valor == 1):
		m6="Se incremento el stock del producto: "+str(codigo)
		modificaStock(idBuscado,1,m6)
		eventos(m6)


def modificaStock(unId, unValor, unMensaje):
	sql = "UPDATE productos SET cantidad = cantidad + %s WHERE id_producto = %s"
	val = (str(unValor),str(unId))
	micursor.execute(sql,val)
	mibase.commit()
	print unMensaje


def nroTransac(): #LEE EL NUMERO DE TRANSACCION ACTUAL DEL ARCHIVO NroTransaccion.csv
	
	global nroTransaccion

	if os.path.isfile(pathNroTransaccion):
		fileReader = open(pathNroTransaccion, 'r')
		reader = csv.reader(fileReader)
		listaNT = list(reader)
		nroTransaccion = int(listaNT[0][0])
		fileReader.close()
		
	else:
		fileWriter = open(pathNroTransaccion, 'w')
		writer = csv.writer(fileWriter)
		writer.writerow([0])
		fileWriter.close()
			

def incrementaNroTransaccion(): #INCREMENTA EN UNA UNIDAD EL NUMERO DE TRANSACCION
	
	fileReader = open(pathNroTransaccion, 'r')
	reader = csv.reader(fileReader)
	listaNT = list(reader)
	listaNT[0][0] = int(listaNT[0][0]) + 1
	global nroTransaccion 
	nroTransaccion = int(listaNT[0][0])

	fileWriter = open(pathNroTransaccion, 'w')
	writer = csv.writer(fileWriter)
	writer.writerows(listaNT)

	fileReader.close()
	fileWriter.close()

		
def estadoSistema():  # Se evalua se el sistema esta HABILITADO o NO (estado.txt 1=HABILITADO, 0= DESHABILITADO)

	bandera = False
	fileReader = open(pathEstadoSistema, 'r')

	if fileReader.read(1) == '0':
		bandera = False
	else:
		bandera = True
	fileReader.close()
	return bandera
	
		
def init(): # Inicializaciones

	global nroTransaccion
	nroTransac()

	os.system('clear')
	m0="Bienvenido al sistema de gestion de stock"
	print (m0)
	eventos(m0)
	resetTempTransaccion()
	resetCodME()

	global flagAceptar
	global flagCancelar
	flagAceptar = False
	flagCancelar = False

	global ser # se inicia el puerto serial 9800,8,N,1
	ser=serial.Serial('/dev/ttyAMA0',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

	global fecha
	fecha = datetime.datetime.now()


# ----------------   Main  -------------------------------	
if __name__ == '__main__':

	init()

	while estadoSistema():
		desactivaGPIO()

		if GPIO.input(25) == False:
			m1='Estado normal\n'
			print (m1)
			eventos(m1)
			activaGPIO()

			while flagCancelar == False and flagAceptar == False and GPIO.input(25) == False:
				modoNormal()
				if flagAceptar:
					aceptar()
				if flagCancelar:
					cancelar()

			desactivaGPIO()

		if GPIO.input(25) == True:
			m2='Estado especial\n'
			print (m2)
			eventos(m2)
			activaGPIO()

			while flagCancelar == False and flagAceptar == False and GPIO.input(25) == True:
				modoEspecial()
				if flagAceptar:
					aceptar()
				if flagCancelar:
					cancelar()

			desactivaGPIO()
	m3="El programa se encuetra deshabilitado"
	print (m3)
	eventos(m3)

# -----------------------   Fin -------------------------------------
