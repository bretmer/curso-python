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

# un empresario de alquiler de autos desea guardar en una base de datos de la informacion de sus vehiculos, proceso que desea automizar con un sistema 
# informatico, las acciones que pueden realizar el empresario son ver las listas de autos que tienen, podra tambien actulizar la lista y agregar un 
# nuevo vehiculo.
# casos de uso
# 1. Ver la lista de autos: El empresario puede consultar la lista completa de autos disponibles en la base de datos.
# 2. Actualizar la lista de autos: El empresario puede modificar la información de un vehículo existente.
# 3. Agregar un nuevo vehículo: El empresario puede añadir nuevos vehículos a la base de datos.
# programacion
lista_autos=[
    {
        "nombre":"supra mk4",
        "marca":"toyota",
        "año":1985
    },{
        "nombre":"GT-R",
        "marca":"nissan",
        "año":1969
    },{
        "nombre":"Golf",
        "marca":"volkswagen",
        "año":1985
    },{
        "nombre":"Q5",
        "marca":"jac",
        "año":1994
    },{
        "nombre":"celia",
        "marca":"hyundai",
        "año":1990
    }]
lista_autos[3]={"nombre":"G-class","marca":"mercedes-benz","año":1979}
lista_autos.insert(5,{"nombre":"A6","marca":"audi","año":1998})

print(lista_autos)

# crear una lista de los primeros 20 numeros primos haciendo uso de comprension

num_primos=[]
lista_nueva=[num_primos for num_primos in range(2,100)if int(num_primos)%2==+1][:20]
print(lista_nueva)