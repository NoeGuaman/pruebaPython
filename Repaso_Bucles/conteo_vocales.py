palabras = ["Ordenador", "Python", "Bucle", "Programación", "Lentejas"]
total = 0

for palabra in palabras:
    cuenta = 0
    for letra in palabra:
        if letra in "aeiou":
            cuenta += 1
    print(palabra, "→", cuenta, "vocales")
    total += cuenta

print("Total de vocales:", total)
