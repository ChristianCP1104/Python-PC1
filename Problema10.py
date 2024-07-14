lista_muestra = ['Rojo','Verde','Blanco','Negro','Rosa','Amarillo']
elementos_eliminar=[0,4,5]
nueva_lista=[lista_muestra[i] for i in elementos_eliminar]
for valor in nueva_lista:
    lista_muestra.remove(valor)
print(lista_muestra)