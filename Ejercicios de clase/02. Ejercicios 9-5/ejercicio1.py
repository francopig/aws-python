
renta = int(input("Ingrese su renta mensual: "))

if renta < 10000:
    print("Su tipo impositivo es del 5%")
elif renta <= 20000:
    print("Su tipo impositivo es del 15%")
elif renta  <= 35000:
    print("Su tipo impositivo es del 20%")
elif renta <= 60000:
    print("Su tipo impositivo es del 30%")
else:
    print("Su tipo impositivo es del 45%")