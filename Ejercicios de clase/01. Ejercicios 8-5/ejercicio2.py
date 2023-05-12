temperaturas = [[10, 15], [19, 19], [10, 19], [3, 15], [2, 15]]
promedios = [];
for temperatura in temperaturas:
    promedios.append( (temperatura[0] + temperatura[1]) / 2 )

print("Temperaturas medias: ")
for i in range(len(promedios)):
    print("Dia ", i+1 , ":", promedios[i]);


#Le asigno la primera
temperatura_minima = temperaturas[0][0] 
dia_frio = None


for i in range(len(temperaturas)):
    if temperaturas[i][0] <= temperatura_minima:
        temperatura_minima = temperaturas[i][0]
        dia_frio = i + 1


print("La temperatura minima fue: ", temperatura_minima)
print("Dia mas frio: ", dia_frio)

temperatura_busca = int(input("Ingrese la temperatura maxima a buscar: "))
for i in range(len(temperaturas)):
    if temperaturas[i][1] == temperatura_busca :
        print("El dia", i+1, "coincide con la temperatura máxima a buscar")

    


