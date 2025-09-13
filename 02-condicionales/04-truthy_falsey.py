

# Truthy
bool(True) # True
bool(False) # False básicamente nos indica si es un valor verdadero o falso

# Falsey

print(bool(True)) # True
print(bool(False)) # False
print(bool(None)) # False equiparable a Null en otros lenguajes
print(bool(0)) # Numero cero False
print(bool(1)) # Numero positivo True
print(bool(-1)) # Numero negativo True
print(bool(1j)) # Numero complejo True
print(bool("")) # String vacío False
print(bool(" ")) # String True (no está vacío como tal, tiene un espacio " ")
print(bool()) # bool vacío False
print(bool(())) # Tupla False
print(bool([])) # Lista False 
print(bool({})) # Diccionario False

"""Por lo tanto todos aquellos True son todos los restantes que no sean False, es decir aquellos que no están vacíos"""



