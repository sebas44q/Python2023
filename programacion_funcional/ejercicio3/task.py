def filtra_lista(funcion, lista):
    '''Función que filtra los elementos de una lista que devuelven true al aplicarle una función booleana.

    Parámetros:
        - funcion: Es una función booleana (devuleve true o false)
        - lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con los elementos de la lista que devuelven true al aplicarles la función booleana.
    '''
# TODO


def par(n):
# TODO


print(filtra_lista(par, [1, 2, 3, 4, 5, 6]))
# resultado esperado [2, 4, 6]

print(filtra_lista(par, [1, 2, 3, 4, 5, 6, 7, 8]))
# resultado esperado [2, 4, 6, 8]
