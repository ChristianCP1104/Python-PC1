def eliminar_duplicados(lista):
    conjunto_sin_duplicados = set(lista)
    lista_sin_duplicados = list(conjunto_sin_duplicados)
    return lista_sin_duplicados

lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

lista_procesada = eliminar_duplicados(lista_original)

print("Lista original:", lista_original)
print("Lista procesada:", lista_procesada)