### EJERCICIOS
## 1
#diseñar un algoritmo que determine si el primero de dos numeros es el mayor
numero_uno:int=int(input("ingrese su primer numero: "))
numero_dos:int=int(input("ingrese su segundo numero: "))
if numero_uno > numero_dos:
    print("el primer numero es el mayor")
else:
    print("el segundo numero es el menor")

## 2
#algoritmo que calcule el promedio de tres numeros
numero1:int=13
numero2:int=7
numero3:int=16
promedio:float=(numero1+numero2+numero3)/3
print(promedio)

## 3
#algoritmo que valide si un numero se encuentra en el rango de 1 a 100
numero_ingresado:int=int(input("ingrese un numero en el rango de 1-100: "))
if numero_ingresado >= 1 and numero_ingresado <= 100:
    print("el numero se encuentra dentro rango ")
else:
    print("el numero esta fuera del rango")

## 4
#algoritmo que calcule el volumen de la esfera
volumen:float=4/3
pi:float=3.1416
radio:int=int(input("ingrese su radio de la esfera: "))
esfera:float=(volumen)*pi*radio**3
print(esfera)

## 5
#algoritmo que me calcule el area de triangulo
base:int=5
altura:int=8
area_triangulo:float=(base*altura)/2
print(area_triangulo)

## 6
#algoritmo que determine un viaje de ida y vuelta al sol a una velocidad costante igual al de la luz
velocidad_luz:int=300000
distancia_sol:int=149597870
viaje_sol:float=(velocidad_luz/distancia_sol)/60
print(viaje_sol*2)

## 7
#algoritmo que valide si un numero es primo o no
numero:int=7
validar:bool=numero%2!=0
print(validar)

## 8
#algoritmo que compare si dos numeros son iguales diferentes o si uno es el doble del otro
primer_numero:int=int(input("ingrese el primer numero: "))
segundo_numero:int=int(input("ingrese el segundo numero: "))
if primer_numero == segundo_numero:
    print("los numeros son iguales")
elif primer_numero != segundo_numero:
    if primer_numero*2 == segundo_numero:
        print("el segundo numero es el doble del primer numero")
    elif segundo_numero*2 == primer_numero:
        print("el primer numero es el doble del segundo numero")
    else:
        print("los numeros son diferentes")

## 9
#algoritmo que calcule el area de un cuadrado
lado_cuadrado:int=9
area_cuadrado:int=lado_cuadrado**2
print(area_cuadrado)

## 10
#algoritmo que convierta de kilometros a millas
kilometros:int=int(input("ingrese el kilometro deseado: "))
millas:float=0.621371
conversion:float=kilometros*millas
print(conversion)

## 11
#escribir un programa  que pregunte el nombre del usuario en la consola y un numero entero e imprima por pantalla
#en lineas distintas el nombre del usuario tantas veces como el numero
nombre:str=input("ingrese su nombre: ")
numero:int=int(input("ingrese un numero entero: "))
print((nombre+ "\n")*numero)

## 12
#escribir un programa que pregunte el nombre completo del usuario en la consola y despues muestre por pantalla el
#nombre completo del usuario tres veces
nombre_completo:str=input("ingrese su nombre completo: ")
print(nombre_completo*3)

## 13
#escribir un programa que pregunte por un numero de telefono con este formato y muestre por pantalla el numero de
#telefono sin el prefijo y la extencion
print("+51-967456789-56")
numero_telefono:str=(input("ingrese su numero de telefono con este formato: "))
print("el numero de telefono es: " , numero_telefono[4:-3])

## 14
#los alumnos se han divido en dos grupos A y B de acuerdo al sexo y nombre. El grupo A esta formado por las mujeres
#con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto
#Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde
nombre_alumno=input("ingrese su nombre: ")
sexo=input("ingrese su sexo como F o M: ")
if sexo == "F":
    if nombre_alumno < "m":
        print("perteneces al grupo A")
    else:
        print("perteneces al grupo B")
else:
    if nombre_alumno > "n":
        print("perteneces al grupo A")
    else:
        print("perteneces al grupo B")

## 15
#escribir un programa que pregunte al usuario la edad del cliente y mostrar el precio de entrada. Si el cliente es menor
#de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar s/.5 y si es mayor de 18 años, s/.10 
edad_cliente:int=int(input("ingrese su edad: "))
if edad_cliente < 4:
    print("su ingreso es gratis")
elif edad_cliente >=4 and edad_cliente <=18:
    print("por su ingreso debe pagar s/.5 ")
elif edad_cliente >18:
    print("por su ingreso debe pagar s/.10")