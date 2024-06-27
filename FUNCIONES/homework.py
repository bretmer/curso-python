# crear una funcion que reciba por argumento n numeros y retorne una lista con los numeros pares
# def numeros_pares(*args):
#     return [n for n in args if n %2==0]
# print(numeros_pares(4,5,6,7,8,9,12,10))


# crear tres funciones para los siguientes casos
# calcular el numero menor
# calcular el numero mayor
# calcular la suma de todos los numeros
# se le pasara por aargumentos n numeros
# def menor(*args):
#     menor=args[0]
#     for n in args:
#         if n<menor:
#             menor=n
#     return menor
# def mayor(*args):
#     mayor=args[0]
#     for n in args:
#         if n>mayor:
#             mayor=n
#     return mayor
# def suma(*args):
#     for n in args:
#         suma+=n
#     return suma
# numeros=2,4,6,8,9,2,3
# print(menor(*numeros))
# print(mayor(*numeros))
# print(suma(*numeros))

# TAREA
# crear una lista de alumnos con los siguiente campos
# nombre, apellido, edad, celular, email
# 1. actualizar los registros con un campo mas todos tendran el campo de programa de estudios de enfermeria 
# 2. buscar el segundo registro y actualizar  su edad a 50 años
lista_alumnos=[
    {
        "nombre":"juan",
        "apellido":"sanches",
        "edad":25,
        "celular":"987546734",
        "email":"juansanches@gmail.com"
    },
    {
         "nombre":"pedro",
        "apellido":"jurado",
        "edad":43,
        "celular":"965712581",
        "email":"pedrojurado@gmail.com"
    },
    {
         "nombre":"sergio",
        "apellido":"peña",
        "edad":30,
        "celular":"912365478",
        "email":"peñasergio@gmail.com"
    },
    {
         "nombre":"lucio",
        "apellido":"solis",
        "edad":35,
        "celular":"987589445",
        "email":"luciosoli@gmail.com"
    }
]
def objeto(a):
    a["programa_estudios"]="Enfermeria"
    return [
        a
    ]
otra_lista=list(map(objeto, lista_alumnos))
print(otra_lista)

def objeto(m):
        m["edad"]=50
        return [
              m
        ]
lista_actualizada=list(filter(objeto, lista_alumnos))
print(lista_actualizada[1])