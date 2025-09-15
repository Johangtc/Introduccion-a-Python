# Instrucciones: 
# Crearás un programa de evaluación de programadores de python para apoyar a RRHH.
# Obtendrás el nombre, los años de experiencia y habilidades.

# Evaluar:
# * Si el candidato sabe Python/Django, tiene +3 años de experiencia: Candidato óptimo.
# * Si el candidato sabe Python/Django, tiene +1 año de experiencia: Buen candidato.
# * Si el candidato sabe Python/Django: Posible candidato.
# * Si el candidato NO sabe Python: Rechazar candidato.

# Consejo, utiliza el método .split()

name = input("Nombre del candidato: ")
experience = int(input("Años de experiencia: "))
skills = input("Ingrese sus habilidades separadas por comas (ej. Python, Laravel, Golang, Django, etc): ").split(",")


evaluate_skills = "Python" in skills or "Django" in skills

result = ""
if evaluate_skills:
    if experience >= 3:
        result = "Candidato optimo"
    elif experience >= 1:
        result = "Buen candidato"
    else:
        result = "Posible candidato"
else:
    result = "No apto, se guardará CV para futuras ofertas"

print(f"El candidato {name} es: {result}")