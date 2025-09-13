

# Evaluar condiciones

# and  (todos los valores sean veraderos)
# Evaluar si dos o más condiciones son verdaderas
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print("\n")
# or  (al menos un valor sea True)
# Evaluar si dos o más condiciones 
print(True or True) # True
print(True or False) # True
print(False or True) # True 
print(False or False) # False

print("\n")
# not (negación)
print(not True) # False
print(not False) # True

print("\n")


"""Ejercicio con and"""
age = 25
is_licensed = True

if age >= 18 and is_licensed:
    print("Puedes conducir")
else:
    print("No puedes conducir")




"""Ejercicio con OR"""
is_student = False
has_membership = True

if is_student or has_membership:
    print("Puedes entrar")
else:
    print("Lo siento, no puedes pasar")




"""Ejercicio con NOT"""
is_admin = False

if not is_admin:
    print("Hola, pasa") # Negativo y negativo da un True
else:
    print("No puedes pasar")


    