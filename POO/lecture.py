# nombre de clase
class mascota:
# atributo de clase
    nombre="leon"
    edad="5 años"
    sexo="macho"
    raza="chihuahua"
# metodos de clase
    def ladrar():
        print("guaa guaa")

# instanciar una clase
labrador=mascota()
labrador.nombre="bobby"
print(labrador.nombre)
aleman=mascota()
aleman.nombre="peruano"
print(aleman.nombre)