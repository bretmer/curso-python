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
# def lista_num():
#     lista_numeros=[63,78,54,567]
#     return min(lista_numeros)
# print(lista_num())

# crear una funcion como parametro el nombre y la edad de una persona mi funcion debera retornar un diccionario
# con los datos, luego mostrar por terminal el valor de retorno en mi funcion.
# nombre="paul"
# edad=43
# def persona(nombre,edad):
#     return{
#         "nombre":nombre,
#         "edad":45
#     }
# print(persona(nombre,edad))

# argumentos posicionales
# def suma(*args):
#     nueva_lista=list(args)
#     nueva_lista[0]=10
#     print(nueva_lista)
# suma(4,7,8,5,2,4)

# # argumentos nominales   
# def alumnos(**kwargs):
#     kwargs["nombre"]="abel"
#     print(kwargs)
# alumnos(nombre="miguel",apellido="largo",edad=30)

# ejemplos de lambda
# saludo=lambda n:f"hola, {n}"
# print(saludo("juan"))

# crear un progama anomino que reciba como parametro una lista de 5 numeros y 
# retorne dos listas, una con numeros pares y otra 
# con numeros impares.
lista=[2,5,6,8,1]
pares,impares = lambda lista: [n for n in lista if n%2==0], lambda lista: [n for n in lista if n%2!=0]
print(pares(lista), impares(lista))


# funcion callback
# def mensaje(m):
#     print(m)
# def pedir_nombre():
#     nombre=input("ingresa tu nombre")
#     return nombre
# mensaje(pedir_nombre())

# funcion map():
# lista=[4,7,8,5,2]
# nueva_lista=list(map(lambda x: x+1, lista))
# print(nueva_lista)

# tengo una lista de alumnos que todos ellos aprabaron y pasan al tercer semestre
# problema en mi lista todos estan con el segundo semestre por lo que tendremos que crear 
# una solucion que cambie el campo de semestre de 2 a 3.
# lista_alumnos=[
#     {
#         "nombre":"abel",
#         "edad":36,
#         "semestre":2
#     },
#     {
#         "nombre":"anthony",
#         "edad":40,
#         "semestre":2
#     },
#     {
#         "nombre":"edith",
#         "edad":50,
#         "semestre":2
#     }
# ]
# def objeto(e):
#     if "semestre" in e:
#         e["semestre"]=e["semestre"]+1
#     e["especialidad"]="arquitectura"
#     return [
#             e
#         ]
# nueva_lista=list(map(objeto , lista_alumnos))
# print(nueva_lista)

# devolver los numeros pares de una lista
# lista_numeros=[4,8,2,5,7,10,6,5,3,20]
# nueva_lista=list(filter(lambda x: x%2==0, lista_numeros))
# print(nueva_lista)

lista_alumnos=[
    {
        "nombre":"abel",
        "edad":36,
        "semestre":2
    },
    {
        "nombre":"anthony",
        "edad":40,
        "semestre":2
    },
    {
        "nombre":"edith",
        "edad":50,
        "semestre":2
    }
]
otra_lista=list(filter(lambda x: x["edad"]<50, lista_alumnos) )
print(otra_lista)