

# in
# not in

# Esta el nueve el el conjunto de números del 1 al 10?, la respuesta es sí
print(9 in range(1,10)) # True
print(11 in range(1,10)) # False

print("\n")

# Lista de frutas
frutas = ["Manzana", "Pera", "Banana", "Naranja"]
print(frutas)

print("manzana" in frutas) # es case sensitive, está buscando a "manzana" y no a "Manzana"
print("Manzana" in frutas) # True

print("Fresa" not in frutas) # True
print("Manzana" not in frutas) # False