palabra = input("Introduce una palabra:")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    cantidad = 0
    for letra in palabra:
        if letra == vocal:
            cantidad += 1
    print("La vocal " + vocal + " aparece " + str(cantidad) + " veces")