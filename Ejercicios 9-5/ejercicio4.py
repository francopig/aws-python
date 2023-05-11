entrada = int(input("Ingrese un numero para construir el traingulo rectangulo: ")) 

# Cantidad de filas
for i in range(1, entrada * 2, 2):

    #Cantidad de caracteres en la fila
    for j in range(i):
        if i % 2 != 0:
            print(i, end="")
    
    if i % 2 != 0:
        print() #avanza a la siguiente linea
  

# El end="" elimina el /n por defecto que tiene el print
