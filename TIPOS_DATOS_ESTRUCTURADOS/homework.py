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

# Ejercicio 2

# crear una lista con 4 diccionarios donde tendrán los datos de sus mascotas (nombre, edad, sexo, raza).
# mostrar la lista con los 4 diccionarios
# editar el 3er registro y cambiarle la edad sin modificar la lista original
# mostrar la lista original y luego la lista con el 3er registro modificado
lista_mascotas=[
    {
        "nombre":"bobi",
        "edad":3,
        "sexo":"macho",
        "raza":"pastor aleman"
    },
    {
        "nombre":"doky",
        "edad":4,
        "sexo":"macho",
        "raza":"rottweiler"
    },
    {
        "nombre":"luna",
        "edad":2,
        "sexo":"hembra",
        "raza":"chihuahua"
    },
    {
        "nombre":"zeus",
        "edad":5,
        "sexo":"macho",
        "raza":"bóxer"
    }
]
print(lista_mascotas)
copia_lista_mascotas=lista_mascotas.copy()
copia_lista_mascotas[2]["edad"]=4
print(copia_lista_mascotas)