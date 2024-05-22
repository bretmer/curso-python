# if estrucuturado
# edad:int=int(input("ingrese su edad: "))
# if edad>=18:
#     print("eres mayor")
# else:
#     print("eres menor")

# if almacenado en variables
# edad_dos:int=int(input("ingrese su edad: "))
# respuesta:str="eres mayor" if edad>=18 else "eres menor"
# print(respuesta)


# crear un programa que me imprima las 5 vocales 
# vocales:str="aeiou"
# for n in range(0,5):
#     print(vocales[n])

# crear un programa que me muestre los 8 primeros numeros pares
# contador=0
# for n in range(1,17):
#      if n%2==0:
#           contador+=1
#           print(f"{n} es el par numero {contador}")

# crear un programa que pida al usuaruio escribir una oracion muestre por la terminal 
# la cantidad de vocales "a" que tiene esa oracion
# oracion:str=input("escriba una oracion: ")
# contador:int=0
# for n in range(0,len(oracion)):
#      if oracion[n]=="a":
#           contador+=1
# print(contador)

# crear un programa que me cuente la cantidad de comas y me muestre sus indices.
# oracion_usuario:str=input("escriba una oracion que contenga comas: ")
# contador_indice:int=0
# for n in range(0,len(oracion_usuario)):
#      if oracion_usuario[n]==",":
#           contador_indice+=1
#           print(f"la coma es encontrada en el indice{n}")
# print(f"la cantidad total de comas encontradas en la oracion es {contador_indice}")

# oracion_usuario:str=input("escriba una oracion que contenga comas: ")
# contador_indice:int=0
# for indice,letra in enumerate(oracion_usuario):
#      if letra ==",":
#           print(f"su indice de la coma es {indice}")
#           contador_indice+=1
# print(f"la cantidad de comas se {contador_indice}  ")

# escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los 
#años que ha cumplido(desde 1 hasta su edad)
# edad:int=int(input("ingrese su edad: "))
# for n in range(1,edad):
#     print(f"ha cumplido un total de {n} años")

# crear un programa que me pida el nombre de tres personas y guarde en una variable global la 
# ultima letra de sus nombres
# mostrar por pantalla la variable global con las tres ultimas letras del nombre de cada persona
# ultima_letra:str=""
# for _ in range(3):
#     nombre:str=input("escriba su nombre: ")
#     ultima_letra+=nombre[-1]
# print(ultima_letra)   

# crear un programa que muestre por terminal las siguiente figura.
# vocales:str="aeiou"
# for n in range(len(vocales)):
#     print(vocales[n]*(n+1))

# condicion=True
# while True:
#     print("hola")

contador=0
while contador <=5:
    print(contador)
    contador+=1
print(f"el valor final{contador}")   

# crear un programa que pida la cantida de notas que se debe registrar luego pedira las notas
# imprimira el promedio
cantidad=input("ingrese la cantidad de notas: ")
suma=0
contador=0
while cantidad:
    notas=input("ingrese sus notas: ")
    contador+=1
    promedio=suma(cantidad*(notas))/cantidad
    print(promedio)
    


