#1. --- Listas y tuplas ---

#! Listas

bandas_rock = ["Led Zeppelin", "The Rolling Stones", "Queen", "AC/DC", "Pink Floyd"]
# Acceso a elementos de la lista
print(bandas_rock[0])  # Salida: Led Zeppelin
print(bandas_rock[2])  # Salida: Queen

# Modificación de elementos de la lista
bandas_rock[1] = "Guns N' Roses"
print(bandas_rock)  # Salida: ["Led Zeppelin", "Guns N' Roses", "Queen", "AC/DC", "Pink Floyd"]

# Agregar elementos a la lista
bandas_rock.append("The Beatles")
print(bandas_rock)  # Salida: ["Led Zeppelin", "Guns N' Roses", "Queen", "AC/DC", "Pink Floyd", "The Beatles"]

# Eliminar elementos de la lista
bandas_rock.remove("AC/DC")
print(bandas_rock)  # Salida: ["Led Zeppelin", "Guns N' Roses", "Queen", "Pink Floyd", "The Beatles"]


#! Tuplas 

# Tupla de libros
libros = ("1984", "Matar a un ruiseñor", "Don Quijote de la Mancha", "sapiens")

# Acceso a elementos de la tupla
print(libros[0])  # Salida: 1984
print(libros[2])  # Salida: Don Quijote de la Mancha

# Intento de modificación de elementos (generará un error)
libros[1] = "Cien años de soledad"

# Concatenación de tuplas
libros_adicionales = ("Cien años de soledad", "Ulises")
todos_los_libros = libros + libros_adicionales
print(todos_los_libros)  # Salida: ("1984", "Matar a un ruiseñor", "Don Quijote de la Mancha", "sapiens", "Cien años de soledad", "Ulises")

# Desempaquetado de una tupla
libro1, libro2, libro3, libro4 = libros
print(libro1)  # Salida: 1984
print(libro2)  # Salida: Matar a un ruiseñor