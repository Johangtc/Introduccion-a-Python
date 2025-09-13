

# Recibe de forma dinámica, el nombre, año de nacimiento, correo y una contraseña
""" Tendrá que generarse un texto de:
    Nombre: "Johan"
    Email: "asfa@saf.com"
    Tendrás n años en 2050
    Tu contraseña es: "contraseña"

"""
nombre = input("Ingresar nombre: ")
email = input("Ingresa tu correo electrónico: ")
año_nacimiento = input("Ingresa tu año de nacimiento: ")
contraseña = input("Ingresa tu contraseña: ")
contraseña_privada = len(contraseña)
edad_2050 = 2050 - int(año_nacimiento)


tarjeta = f""" 
    Nombre: {nombre}
    Email: {email}
    Tendrás {edad_2050} años en 2050
    Tu contraseña es: {"*" * contraseña_privada}

"""

print(tarjeta)