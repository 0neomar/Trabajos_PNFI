#!/usr/bin/env python3
#--------------------------------------
# Name:        TabFrec
#
# Author:      Neomar Rodriguez
# coding:      UTF-8
# Copyright:   (c) Neomar Rodriguez 2020
# Licence:     <GPLv3>
#--------------------------------------



from math import log10   # Logaritmo.
from math import ceil  # Redondeo hacia arriba.
from math import floor # Redondeo hacia abajo.

from os import system
from itertools import zip_longest
from collections import Counter


from sys import platform
# Para limpiar la consola.
limpiar = lambda: system('cls' if 'win' in platform else 'clear')

### Leyenda:
# n: Numero de datos.
# R: Rango.
# K: Intervalos.
# A: Amplitud.
# x: Marca de clase.
# f: Frecuencia absoluta.
# fr: Frecuencia relativa.
# F: Frecuencia absoluta acumulada.


SIMBOLO_SIGMA = "\N{N-ARY SUMMATION}"

###========================###
###  FUNCIONES NECESARIAS  ###
###========================###

def imprimir_tabla(titulos, filas, padding=0, sepver=True, sephor=True):
	"""
	Imprime la tabla de frecuencias.

	titulos: lista de str.
	filas: lista de listas.
	padding: int, el espacio para centrar el texto.
	sepver: Separar filas con linea vertical.
	sephor: Separar columnas con linea horizontal.
	"""

	if sephor:
		separador_hor = '|'
	else:
		separador_hor = ''

	encabezado = separador_hor
	for titulo in titulos:
		encabezado += titulo.center(padding) + separador_hor

	linea_sep = len(encabezado)*'-' # Linea para separar filas.

	if sepver:
		print(linea_sep, encabezado, linea_sep, sep='\n')
	else:
		print(encabezado)

	for fila in filas:
		print(separador_hor, end='')
		for dato in fila:
			print(str(dato).center(padding), separador_hor, sep='', end='')
		print()

	if sepver:
		print(linea_sep)


def calcular_K(n):
	"""
	Acepta el numero de datos (int).
	Regresa el numero intervalos, redondea hacia un numero impar.
	"""

	# Formula: 1 + 3.322 * log n
	K_decimal = 1+3.322 * log10(n)# logaritmo de n con base 10.

	# Si el redondeo hacia abajo es impar, regresar ese valor.
	if floor(K_decimal) % 2 != 0:
		return floor(K_decimal)

	# Si no redondear hacia arriba.
	return ceil(K_decimal)

def calcular_x(rangos):
	# x = list()
	# for rango in rangos:
	# 	x.append(sum(rango)/2)
	# return x
	return [sum(rango)/2 for rango in rangos]

def calcular_intervalos(datos, A):
	"""
	Regresa una lista de tuplas,
	cada tupla contiene un par de numeros.

	datos: Lista de numeros.
	A: Numero.
	"""
	rangos = list()
	Li = min(datos)  # Limite inferior.
	Ls = Li + A      # Limite superior (inferior mas la amplitud).
	Xmax = max(datos)

	while Ls <= Xmax:
		#grupos.append(['[%s-%s)'%(Li, Ls)])
		rangos.append((Li, Ls))

		Li = Ls
		Ls = round(Ls+A, 2)

	rangos.append((Li, Ls))
	return rangos

def calcular_f(datos, rangos):
	"""
	Regresa una lista con veces que aparece un rango.

	datos: Lista de numeros.
	rangos: lista de listas.
	"""
	contador = Counter(datos)

	f = list()
	for rango in rangos:
		suma = 0
		for i in range(*rango):
			suma += contador[i]
		f.append(suma)

	return f

def calcular_fr(f, n):
	"""
	Regresa una lista con la frecuencia relativa.

	f: Lista de numeros.
	n: int.
	"""
	# fr = list()
	# for i in f:
	# 	fr.append(round(i/n, 2))
	# return fr
	return [round(i/n, 2) for i in f]

def calcular_F(f):
	"""
	Regresa un lista con las frecuencias absolutas acumuladas.

	f: Lista de numeros.
	"""
	F = list()
	suma = 0
	for i in f:
		suma += i
		F.append(suma)
	return F

def calcular_xf(x,f):
	"""
	Regresa la mutiplicacion entre pares de items
	en las listas 'x' y 'f'.

	x: Lista de numeros.
	f: Lista de numeros.
	"""
	# xf = list()
	# for par in zip_longest(x,f, fillvalue=1):
	# 	xf.append(par[0] * par[1])
	# return xf
	return [par[0]*par[1] for par in zip_longest(x,f, fillvalue=1)]

def solicitar_datos():
	"""
	Solicita los datos uno a uno.
	"""
	cantidad_de_datos = int(input('cantidad_de_datos: '))
	datos = list()
	contador = 1
	while len(datos) < cantidad_de_datos:
		try: # Intentar.
			dato = float(input('%s) Dato: '%contador))
		except ValueError: # En caso de ingreso no numerico.
			print('Dato incorrecto!')
			continue  # Saltar a la siguiente iteracion.
		datos.append(dato)
		contador += 1  # Siguiente dato.
	return datos



DATOS_DE_PRUEBA = [
	22, 19, 16, 13, 18, 15, 20, 14, 15, 16,
	15, 16, 20, 13, 15, 18, 15, 13, 18, 15
]

DATOS_2 = [
	36, 30, 47, 60, 32, 35, 40, 50,
	54, 35, 45, 52, 48, 58, 60, 38,
	32, 35, 56, 48, 30, 55, 49, 39,
	58, 50, 65, 35, 56, 47, 37, 56,
	58, 50, 47, 58, 55, 39, 58, 45
]

datos = DATOS_2

#datos = solicitar_datos()
limpiar()
datos.sort()
datos = tuple(
			map(int, datos) # Aplicar int() a cada item en datos.
)

# La cantidad de datos.
n = len(datos)

# El rango.
R = max(datos) - min(datos)

# Los intervalos.
K = calcular_K(n)

# La amplitud.
A = round(R/K) # Redondear division.


# Calcular datos de cada columna.
rangos = calcular_intervalos(datos, A)
x  = calcular_x(rangos)
f  = calcular_f(datos, rangos)
fr = calcular_fr(f, n)
F  = calcular_F(f)
xf = calcular_xf(x, f)

# Dar formato a las clases.
clases = list()
for rango in rangos:
	clases.append('%s-%s' % rango) # rango es una tupla con dos numeros.


titulos = ('clases', 'x', 'f', 'fr', 'F', 'x.f')

imprimir_tabla(
	titulos,
	zip_longest(clases, x, f, fr, F, xf, fillvalue=''),
	padding=9,
)


# Imprimir los totales
sumatorias = (
	SIMBOLO_SIGMA,
	'',
	str(sum(f)),
	str(sum(fr)),
	'',
	str(sum(xf))
)

imprimir_tabla(
	sumatorias,
	[],
	padding=9,
	sepver=False
)

print('\nMEDIA X\u203e:', sum(xf)/n, '\n')

