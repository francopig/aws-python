# Escribir un programa que pida al cliente una palabra e imprima el número de veces que contiene cada vocal.

clave = input("Ingrese una clave: ")

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for letra in clave:
    if letra == "a":
        contador_a += 1
    elif letra == "e":
        contador_e += 1
    elif letra == "i":
        contador_i += 1
    elif letra == "o":
        contador_o += 1
    elif letra == "u":
        contador_u += 1
    

print("cantidad de a: ",contador_a)
print("cantidad de e: ",contador_e)
print("cantidad de i: ",contador_i)
print("cantidad de o: ",contador_o)
print("cantidad de u: ",contador_u)

