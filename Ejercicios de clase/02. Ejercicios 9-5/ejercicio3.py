
frase = input("🤠 Ingrese una frase: ")
letra = input("🤠 Ingrese una letra: ")

contador = 0

for caracter in frase:
    if(letra == caracter):
        contador += 1

print(f"Aparece {contador} veces la letra {letra} en la frase '{frase}'")