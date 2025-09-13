

# El operador ternario es un if-else en una sola línea

is_student = True

print("\n-----Con if-else-------")

if is_student:
    print("Licencia estudiantil")
else:
    print("Licencia normal")
    
print("\n-----Con operadores ternarios-------")

# True if condition else False

get_license = "Licencia estudiantil" if is_student else "Licencia normal" 
print(get_license)