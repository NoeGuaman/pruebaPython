clave = "python"
intento = input("Introduce la contraseña: ")

while intento != clave:
    print("Incorrecto. Intenta de nuevo.")
    intento = input("Introduce la contraseña: ")

print("Acceso concedido.")
