# # return devuelve valores que podre hacer uso
# # crear una funcion que retorne el numero 10, y muestre por
# # terminal si es par
# def diez():
#     return 10
# if diez()%2==0:
#     print("es par")
# else:
#     print("es impar")
# # print solo muestra por terminal

# # crear una funcion que me muestre el producto de dos numeros
# def producto(a,b):
#     return a*b

# # crear una funcion que me retone una lista de tres numeros
# def lista_numeros():
#     return[3,4,5]

# ###  print usaremos cada vez que nuestra funcion retorne un mensaje
# # crer una funcion que por parametro reciba un nimbre y retorne un mensaje
# # de bienvenida con el nombre
# def mensaje(nombre):
#     print(f"hola {nombre} bienvenido al chongo")

# crear una funcion que reciba por parametros una lista de numeros y me devuelva el numero menor,
# mostrar por terminal el valor retornando la funcion
def lista_num():
    lista_numeros=[63,78,54,567]
    return min(lista_numeros)
print(lista_num())

# crear una funcion como parametro el nombre y la edad de una persona mi funcion debera retornar un diccionario
# con los datos, luego mostrar por terminal el valor de retorno en mi funcion.
nombre="paul"
edad=43
def persona(nombre,edad):
    return{
        "nombre":nombre,
        "edad":45
    }
print(persona(nombre,edad))