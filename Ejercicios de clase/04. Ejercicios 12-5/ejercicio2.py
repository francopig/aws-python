# Función que recibe 3 strings, se busca el segundo string dentro del primero y se reemplaza por el tercero.

def reemplazador(str1,str2,str3):

    respuesta = ""
    for i in range(len(str1)):
        if str1[i] == str2:
            respuesta += str3
        else:
            respuesta += str1[i]
    return respuesta


print(reemplazador("FrancoPig","a","x")) # FrxncoPig
