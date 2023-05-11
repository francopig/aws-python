"""
Escribir un programa que almacene una clave en una variable, 
luego solicite al usuario ingresar una clave válida e imprimir "clave correcta" 
cuando se cumpla la validación sea correcta
"""

clave = "clave123"

entrada = input("Ingresar la clave: ")

if clave == entrada:
    print("La clave ingresa coincide ✔")
else:
    print("La clave ingresada no coincide ❌")
