notas = [["Matematicas", None], ["Fisica", None], ["Quimica", None], ["Historia", None], ["Lengua", None]]

notas[0][1] = int(input("Ingrese su nota en Matematicas: "));
notas[1][1] = int(input("Ingrese su nota en Fisica: "));
notas[2][1] = int(input("Ingrese su nota en Quimica: "));
notas[3][1] = int(input("Ingrese su nota en Historia: "));
notas[4][1] = int(input("Ingrese su nota en Lengua: "));


print("Tiene que repetir las siguientes materias: ")
for i in range(len(notas)):
    if notas[i][1] < 5:
        print(notas[i][0])

