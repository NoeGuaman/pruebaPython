frase = input("Frase a cifrar: ").lower()
cifrada = ""

for letra in frase:
    if letra.isalpha():
        nueva_letra = chr(((ord(letra) - 97 + 2) % 26) + 97)
        cifrada += nueva_letra
    else:
        cifrada += letra

print("Frase cifrada:", cifrada)
