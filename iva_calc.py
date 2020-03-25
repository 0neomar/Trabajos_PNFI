#### COMPATIBILIDAD PARA PYTHON 2 y 3 #####
from __future__ import print_function     #
try: input = raw_input                    #
except NameError: pass                    #
###########################################


__author__ = 'Neomar Rodriguez - CI: 27.944.863'

### EJERCICIO ###
#
# Un supermecado necesita saber el precio real con IVA de sus productos,
#  para lo cual necesita registrar el:
#  - Nombre del producto.
#  - Precio del producto.
#  - Tipo de producto, pueden ser:
#
# 1- Medicina: Tiene un IVA del 5% para los productos que cuestan < 100 Bs,
#     los productos que cuestan Bs 100 o mas tendran un IVA del 3%.
#
# 2- Comida: Tiene un IVA del 10% para los productos que son mayor o
#     igual a 200 Bs, los productos que cuestan menos de 200 Bs
#     tendran un IVA del 15%.
#
# 3- Otros: Tiene un IVA del 16%.
#
# El programa final debera mostrar:
#  1. Nombre del producto.
#  2. Precio original sin IVA.
#  3. El IVA calculado al precio original
#  4. El total + el IVA calculado.
#
# Utilizar: IF, ELIF, ELSE, AND, OR.


# Solicitar el nombre usando input.
nombre = input('\nIngrese nombre del producto: ')

# Solicitar el precio con input y convertir a tipo flotante.
precio = float(input('Ingrese precio Bs: '))

# Imprimir un mensaje con los tipos de productos.
print("""
Tipos de productos:
-------------------
1 - Medicina
2 - Comida
3 - Otros
""")

# Solicitar el tipo de producto y convertir a tipo entero.
tipo = int(input('Ingrese tipo de producto: '))


### MEDICINA
# Si el tipo es igual a 1 y el precio menor que cien:
if tipo == 1 and precio < 100:
	# IVA sera igual al 5% del precio.
	IVA = precio * .05

# Si el tipo es igual a 1 y el precio es mayor o igual a cien:
elif tipo == 1 and precio >= 100:
	# IVA sera igual al 3% del precio.
	IVA = precio * .03

### COMIDA
# Si el tipo es igual a dos y el precio es menor a doscientos:
elif tipo == 2 and precio < 200:
	# IVA sera igual al 15% del precio.
	IVA = precio * .15

# Si el tipo es igual a dos y el precio es mayor o igual a doscientos:
elif tipo == 2 and precio >= 200:
	# IVA es igual al 10% del precio.
	IVA = precio * .10

### OTROS

# De lo contrario,
else:
	# IVA sera igual al 16% del precio.
	IVA = precio * .16

# Se crea una cadena de caracteres con 50 guiones.
SEPARADOR = '-' * 50

# Se imprime un salto de linea y una linea separadora.
print('\n', SEPARADOR, sep='')

# Imprimir los titulos, centrando cada valor.
print(
	'', # Primer valor vacio para que se inserte un separador antes del primer valor.
	'NOMBRE'.center(11), # str.center: Centrar texto con ancho fijo 11.
	'PRECIO'.center(11),
	'IVA'.center(11),
	'TOTAL'.center(11),
	sep='|'  # sep: Caracter para separar cada valor.
	)

# Imprimir otra linea separadora.
print(SEPARADOR)

# Imprimir los datos del producto.
print(
	'',  # Primer valor vacio.
	nombre.center(11),       # Centrar los valores.
	str(precio).center(11),  # Convertir los datos a str y luego centrar.
	str(IVA).center(11),
	str(precio+IVA).center(11),
	sep='|'  # Separar valores con barra horizontal.
	)

# Imprimir una ultima linea separadora.
print(SEPARADOR)
