def reemplazador(str1, str2, str3):
    respuesta = ""
    i = 0
    while i < len(str1):
        if str1[i:i+len(str2)] == str2:
            respuesta += str3
            i += len(str2)
        else:
            respuesta += str1[i]
            i += 1
    return respuesta

print(reemplazador("FrancoPig","an","uwu")) #FruwucoPig
