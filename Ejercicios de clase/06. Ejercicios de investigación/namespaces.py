

# Definición del espacio de nombres "geometria"
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14159 * self.radio**2

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

# Uso de los espacios de nombres
circulo = geometria.Circulo(5)
print("Área del círculo:", circulo.area())

rectangulo = geometria.Rectangulo(4, 6)
print("Área del rectángulo:", rectangulo.area())