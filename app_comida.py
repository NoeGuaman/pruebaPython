from datetime import datetime

hora_actual = datetime.now().hour
#hora_actual = int(input("Dime la hora: "))

if hora_actual >= 6 and hora_actual < 12:
    print("Es de mañana")
    print ("Que quieres desayunar")
    print ("1. Huevos")
    print ("2. Café con tostadas")
    comida = int(input("Seleccionalo con el numero"))
    if comida == 1:
        print ("Has elegido huevos")
    elif comida == 2:
        print ("Has cafe con tostadas")
    else:
        print("No hay desayuno")
elif hora_actual >= 12 and hora_actual < 18:
    print("Es de tarde ")
elif hora_actual >= 18 and hora_actual < 22:
    print("Es de noche")
else:
    print("Es de madrugada ")
