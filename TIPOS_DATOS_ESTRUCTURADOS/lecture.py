# texto="hola"
# lista_texto=list(texto)
# lista2=[e for e in texto]

texto_largo="este es un texto largo chiquitas y chiquitos"
nueva_lista=texto_largo.split(" ")
print(" ".join(texto_largo))

# dato primitivo
nombre="abel"
print(id(nombre))
otro_nombre=nombre
print(id(otro_nombre))

# datos estructurados
lista_original=[1,2,3,4]
copia_lista=lista_original # copia la referncia o la direccion de la lista

lista_original[-1]=15
print(copia_lista)

# crear un programa que reciba una lista desordenada, y muestre por terminal la lista oredenada y la lista previa a ser ordenada.
lista=[1,4,6,5]
copia_lista=lista.copy() # copia el valor de la lista
copia_lista.sort() # ordena los valores de la lista
print(lista)
print(copia_lista)
