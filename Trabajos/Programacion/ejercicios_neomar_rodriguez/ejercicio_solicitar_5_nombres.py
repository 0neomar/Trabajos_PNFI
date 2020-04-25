# Encoding: UTF-8
# Author: Neomar Rodriguez - 27.944.863


# Inicializar las listas.
nombres, edades = [], []

for i in range(1,6):
	# Solicitar los datos.
	nombres.append(input("Nombre %s: "%i))
	edades.append(int(input("Edad %s: "%i)))
	print()

# Obtener el indice de la persona mayor y menor, respectivamente.
max_edad_i = edades.index(max(edades))
min_edad_i = edades.index(min(edades))

# Imprimir el nombre y la edad que se encuentren en esos indices.
print("La persona mayor es %s con %s años de edad."%(nombres[max_edad_i], edades[max_edad_i]))
print("La persona menor es %s con %s años de edad."%(nombres[min_edad_i], edades[min_edad_i]))
