num = int(input("Introduce un número (0 para salir): "))
mayor = 0
while num != 0:
    if num > mayor:
        mayor = num
    num = int(input("Introduce un número: "))
if num == 0 and mayor == 0:
    print("No hay números mayores")
else:
    print("El mayor número fue:", mayor)