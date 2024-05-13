# # if estrucuturado
edad:int=int(input("ingrese su edad: "))
if edad>=18:
    print("eres mayor")
else:
    print("eres menor")

# # if almacenado en variables
edad_dos:int=int(input("ingrese su edad: "))
respuesta:str="eres mayor" if edad>=18 else "eres menor"
print(respuesta)


# crear un programa que me imprima las 5 vocales 
vocales:str="aeiou"
for n in range(0,5):
    print(vocales[n])

# crear un programa que me muestre los 8 primeros numeros pares
contador=0
for n in range(1,17):
     if n%2==0:
          contador+=1
          print(f"{n} es el par numero {contador}")

# # crear un programa que pida al usuaruio escribir una oracion muestre por la terminal 
# la cantidad de vocales "a" que tiene esa oracion
oracion:str=input("escriba una oracion: ")
contador:int=0
for n in range(0,len(oracion)):
     if oracion[n]=="a":
          contador+=1
print(contador)

# crear un programa que me cuente la cantidad de comas y me muestre sus indices.
oracion:str=input("escriba una oracion: ")
contador=0
for n in range(0,len(oracion)):
     if oracion[n]==",":
          contador+=1
          print(f"coma encontrada en el indice{n}")
print(contador)



