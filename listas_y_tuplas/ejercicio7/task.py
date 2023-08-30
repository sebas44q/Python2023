palabra = input("Introduce una palabra:")
palabra_rev = palabra
palabra = list(palabra)
palabra_rev = list(palabra_rev)
palabra_rev.reverse()

if palabra ==palabra_rev:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")