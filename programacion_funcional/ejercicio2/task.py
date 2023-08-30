def aplica_funcion_lista(funcion, lista):
    '''Función que aplica una función a todos los elementos de una lista.

    Parámetros:
        funcion: Es una función.
        lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con el resultado de aplicar la función a los valores de la lista.
    '''
# TODO


def cuadrado(n):
# TODO


print(aplica_funcion_lista(cuadrado, [1, 2, 3, 4]))

# resultado esperado [1, 4, 9, 16]

print(aplica_funcion_lista(cuadrado, [1, 2, 3, 4, 5]))
# resultado esperado [1, 4, 9, 16, 25]
