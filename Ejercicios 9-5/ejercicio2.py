
edad = int(input("Por favor, ingrese la edad del cliente: "))

if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10

print("El precio de entrada para el cliente es de", precio, "euros.")