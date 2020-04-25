# Encoding: UTF-8
# Author: Neomar Rodriguez - 27.944.863


# Preguntar sobre que tablas ver.
ver_sumas = ('s' in input('¿Ver tabla de suma?: ')) # True si hay una 's'
ver_restas = ('s' in input('¿Ver tabla de restas?: '))
ver_multiplicaciones = ('s' in input('¿Ver tabla de multiplicaciones?: '))

num_a_operar = int(input('Numero a operar: '))

if ver_sumas:
	print('\nTabla de Sumas')
	print('-'*20)
	for i in range(1,11):
		print('%s + %s = %s'%(num_a_operar, i, num_a_operar+i))

if ver_restas:
	print('\nTabla de Restas')
	print('-'*20)
	for i in range(1,11):
		print('%s - %s = %s'%(num_a_operar, i, num_a_operar-i))

if ver_multiplicaciones:
	print('\nTabla de Multiplicaciones')
	print('-'*20)
	for i in range(1,11):
		print('%s * %s = %s'%(num_a_operar, i, num_a_operar*i))

