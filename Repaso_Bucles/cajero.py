saldo = 1000
operacion = ""

while operacion.lower() != "salir":
    print(saldo)
    operacion = input("¿Deseas ingresar, retirar o salir?: ")
    if operacion.lower() == "ingresar":
        cantidad = int(input("¿Cuánto deseas ingresar: "))
        saldo += cantidad
    elif operacion.lower() == "retirar":
        cantidad = int(input("¿Cuánto deseas retirar: "))
        if cantidad <= saldo:
            saldo -= cantidad
        else:
            print("Saldo insuficiente")
print("Hasta otra")