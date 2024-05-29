# Ejercicio 1:
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
        "nombre":"abel",
        "apellido":"jurado",
        "edad":24
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
lista_alumnos.pop(3)
print(lista_alumnos)
# buscar y mostrar el de la psicion 4 de la lista
indice=lista_alumnos.index({
    "nombre":"percy",
    "apellido":"yarihuaman",
    "edad":25
})
print(lista_alumnos[indice])