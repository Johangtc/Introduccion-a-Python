

print(5 == 5) # True
print(1 == True) # True 
print("" == True) # False

new_list = []
other_list = []

print(new_list == other_list) # True
print(new_list is other_list) # False

# is es un operador de identidad
# Verifica el objeto en la MEMORIA

a = None
b = None

print(a is b) # Comunmente se utiliza un None, True, False para saber la identidad