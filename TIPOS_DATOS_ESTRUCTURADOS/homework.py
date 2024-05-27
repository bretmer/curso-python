# crear una lista de 5 alumnos cada alumno almacenaremos su nombre apellido y edad
# insertrar al final de la listalos datos de antony
# eliminar de la lista si existe los datos de abel
# buscar y mostrar el alumno en la posicion 4 de la lista 
lista_alumnos=[
    {
        "nombre":"sergio",
        "apellido":"barrientos",
        "edad":20,
    },{
        "nombre":"ronald",
        "apellido":"valencia",
        "edad":13,
    },{
        "nombre":"sergio",
        "apellido":"perez",
        "edad":80
    },{
        "nombre":"ronny",
        "apellido":"roman",
        "edad":19
    },{
        "nombre":"percy",
        "apellido":"yarihuaman",
        "edad":25
    }
]
nueva_lista=[
    {"nombre":"antony",
    "apellido":"cruzes",
    "edad":30
    }
]
lista_alumnos.append(nueva_lista)
print(lista_alumnos)

