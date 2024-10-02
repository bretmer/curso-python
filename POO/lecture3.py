class Alumno:
    def __init__(self,dni,nombre,apellido,edad,genero,):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.genero=genero

    def escribir(self):
        print("estoy escribiendo")
    def tarea(self,nobre_docente):
        print("haciendo la tarea de:",nobre_docente)
    def terminar_tarea(self):
        print("terminado tarea")


jorge=Alumno(70873465,"jorge","peña",21,"M")
jorge.tarea


# print(jorge.nombre)

# luna=Alumno(76365412,"luna","lince",19,"F")
# print(luna.genero)

# oliver=Alumno(45374743,"oliver","reyes",20,"F")
# print(oliver.edad)

# chistian=Alumno(75674743,"chistian","cueva",37,"M")
# print(chistian.apellido)