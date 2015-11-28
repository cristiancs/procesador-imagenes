
from funciones import *
import os.path
import random
from math import sqrt
def createMatriz(archivo):
	fileName = archivo.split('.')[0]
	if os.path.exists(fileName+'.txt'):
		matriz = leerArchivo(fileName+'.txt')
	else:
		print "Creando Matriz"
		convertirImagenAArchivo(archivo,fileName+'.txt')
		matriz = leerArchivo(fileName+'.txt')
		print "Procesando Imagen"
	return matriz
def EscaladeGrises(archivo):
	fileName = archivo.split('.')[0]
	matriz = createMatriz(archivo)
	nuevaImagen = []
	x1,y1 = 0,0
	for x in matriz:
		y1 = 0
		nuevaImagen.append([])
		for y in x:
			r,g,b = y
			valor = int((r+g+b)/3)
			nuevaImagen[x1].append((valor,valor,valor))
			y1+=1
		x1 +=1
	convertirMatrizAImagen(nuevaImagen,fileName+'-gray.jpg')

def Negativo(archivo):
	fileName = archivo.split('.')[0]
	matriz = createMatriz(archivo)
	nuevaImagen = []
	x1,y1 = 0,0
	for x in matriz:
		y1 = 0
		nuevaImagen.append([])
		for y in x:
			r,g,b = y
			nuevaImagen[x1].append((255-r,255-g,255-b))
			y1+=1
		x1 +=1
	convertirMatrizAImagen(nuevaImagen,fileName+'-negativo.jpg')

def FiltroOriginal(archivo,color,tolerancia):
	fileName = archivo.split('.')[0]
	matriz = createMatriz(archivo)
	nuevaImagen = []
	x1,y1 = 0,0
	for x in matriz:
		y1 = 0
		nuevaImagen.append([])
		for y in x:
			r,g,b = y
			diff = sqrt(1.4*(r-color[0])**2 + .8*(g-color[1])**2 + .8*(b-color[2])**2) 
			if diff > tolerancia:
				valor = int((r+g+b)/3)
				nuevaImagen[x1].append((valor,valor,valor))
			else:
				nuevaImagen[x1].append((r,g,b))
			y1+=1
		x1 +=1
	convertirMatrizAImagen(nuevaImagen,fileName+'-filtro.jpg')
def Filtro2(archivo):
	fileName = archivo.split('.')[0]
	matriz = createMatriz(archivo)
	nuevaImagen = []
	cont=0
	for x in matriz[0]:
		nuevaImagen.append([])
		cont+=1
	ancho=len(x)
	largo=cont
	for x in matriz:
		i=0
		for y in range(largo):
			x=list(reversed(x))
			nuevaImagen[y].append(tuple(x[i]))
			i+=1	
	convertirMatrizAImagen(nuevaImagen,fileName+'-filtro2.jpg')
	RotarImagen(fileName+'-filtro2.jpg',90,False)
def Filtro3(archivo,color,tolerancia):
	fileName = archivo.split('.')[0]
	matriz = createMatriz(archivo)
	nuevaImagen = []
	x1,y1 = 0,0
	for x in matriz:
		y1 = 0
		nuevaImagen.append([])
		for y in x:
			r,g,b = y
			diff = sqrt(1.4*(r-color[0])**2 + .8*(g-color[1])**2 + .8*(b-color[2])**2) 
			if diff > tolerancia:
				nuevaImagen[x1].append((255-r,255-g,255-b))
			else:
				nuevaImagen[x1].append((r,g,b))
			y1+=1
		x1 +=1
	convertirMatrizAImagen(nuevaImagen,fileName+'-filtro3.jpg')
def RotarImagen(archivo,grados,editName=True):
	fileName = archivo.split('.')[0]
	matriz = createMatriz(archivo)
	nuevaImagen = []
	# 
	if grados==90:
		matriz=list(reversed(matriz))
		cont=0
		for x in matriz[0]:
			nuevaImagen.append([])
			cont+=1
		ancho=len(x)
		largo=cont
		for x in matriz:
			i=0
			for y in range(largo):
				nuevaImagen[y].append(tuple(x[i]))
				i+=1
	if grados==180:
		nuevaImagen=list(reversed(matriz))
		for x in range(len(nuevaImagen)):
			nuevaImagen[x] = list(reversed(nuevaImagen[x]))
	if grados==270:
		matriz=list(matriz)
		cont=0
		for x in matriz[0]:
			nuevaImagen.append([])
			cont+=1
		largo=cont
		for x in (matriz):
			i=1
			for y in range(largo):
				nuevaImagen[y].append(tuple(x[largo-i]))
				i+=1
	if grados=='espejo-horizontal':
		for x in range(len(matriz)):
			nuevaImagen.append(list(reversed(matriz[x])))
	if grados=='espejo-vertical':
		nuevaImagen=list(reversed(matriz))	
	if(editName):
		convertirMatrizAImagen(nuevaImagen,fileName+'-rotada-'+str(grados)+'.jpg')
	else:
		convertirMatrizAImagen(nuevaImagen,fileName+'.jpg')
def DoAll(fileName,filtroColor):
	EscaladeGrises(fileName)
	Negativo(fileName)
	RotarImagen(fileName,90)
	RotarImagen(fileName,180)
	RotarImagen(fileName,270)
	RotarImagen(fileName,'espejo-horizontal')
	RotarImagen(fileName,'espejo-vertical')
	FiltroOriginal(fileName,filtroColor,130)
	Filtro2(fileName)
	Filtro3(fileName,filtroColor,130)
# DoAll('_MG_2082.JPG',(178, 180, 103))
# FiltroOrigina	`	l('_MG_2082.JPG',(178, 180, 103),30)


EscaladeGrises('logo-usm.jpg')
Negativo('logo-usm.jpg')
RotarImagen('logo-usm.jpg',90)
RotarImagen('logo-usm.jpg',180)
RotarImagen('logo-usm.jpg',270)
RotarImagen('logo-usm.jpg','espejo-horizontal')
RotarImagen('logo-usm.jpg','espejo-vertical')
FiltroOriginal('logo-usm.jpg',(251, 145, 8),100)
Filtro2('logo-usm.jpg')
Filtro3('logo-usm.jpg',(251, 145, 8),100)

print "Terminado"
