# Definir una función que reciba una cierta cantidad de números y los retorne ordenados. Si recibe letras las borra. Los números repetidos no se eliminan.

def ordenar(cadena):

   #quitamos caracteres
   limpio = ""
   for caracter in cadena:
    if caracter.isdigit():
        limpio += caracter


    #ordenamos
    ordenado = ""
    for h in range(len(cadena)):
        for i in range(len(cadena)):
            if cadena[i] == str(h):
                ordenado += str(h)

    return(ordenado)

print(ordenar("01010101"))
print(ordenar("01242151235"))
print(ordenar("01q+242aa15123r"))


