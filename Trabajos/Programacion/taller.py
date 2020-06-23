__integrantes__ = {
	"27.216.702": "MARQUEZ ADRIAN",
	"27.944.863": "RODRIGUEZ NEOMAR",
	"29.669.993": "MENDEZ YAIFRAN",
	"30.637.496": "SERENO JOSE",
}

numeros_neg = []
numeros_pos = []
contador_ceros = 0

for i in range(10):
	n = int(input("Ingresar numero: "))

	if n < 0:
		numeros_neg.append(n)
	elif n > 0:
		numeros_pos.append(n)
	else:
		contador_ceros += 1
		print("Numero neutro, no se guardara\n")


print("-" * 40)

print("No se ingresaron ceros." if contador_ceros==0 else "Se ingreso %s cero(s)"%contador_ceros)

print("\nPositivos:")
print(*numeros_pos if numeros_pos else ["Ninguno"], sep="\t")

print("\nNegativos:")
print(*numeros_neg if numeros_neg else ["Ninguno"], sep="\t")

