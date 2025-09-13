

name = "Javi"
print(name) # Javi

# ¿En qué posición se encuentra ubicada cada letra?
"""
J a v i
0 1 2 3

"""

# Por lo tanto "Javi" tiene 3 caracteres (no 4, ya que es en base al 0)

print(name[0])
print(name[1])
print(name[2])
print(name[3])

print("\n---------")
# Pero si me llamo Maximiliano? y quiero la última letra del nombre

nombre_largo = "Maximiliano"
print(nombre_largo[-1]) # "o"

# y ahora un start:stop, quiero las primeras 3 letras del nombre?
print(nombre_largo[0:3]) # "Max"

# y si ahora quiero que omita la "a" de "Max"?

# start:stop:stepover
print(nombre_largo[0:3:2]) # "Mx"

print("\n---------")
"""Poner tu nombre al revés, si te llamas Carmela, tendrá que decir alemraC"""

mi_nombre = "Johan"

print(mi_nombre[-1:-4:-1]) #no funcionaría

print("\n---------")

# Usaremos un ::1 para pedir toda la cadena
print(mi_nombre[::1]) # Johan, así que si aplicamos el -1 para empezar desde el final...
print(mi_nombre[::-1]) # nahoJ