### EJERCICIOS 1
## 1
#hacer un programa que determine si un numero introducido por el usuario tiene una longitud
#mayor o igual que 3 y a su vez es menor que 10
numero_ingresado:str=(input("por favor ingrese un numero: "))
longitud_numero=len(numero_ingresado)
comparacion= longitud_numero >= 3 and longitud_numero < 10
print(comparacion)

## 2
#guardamos en una variable numero_magico
numero_magico:str="12345679"
#pedimos al usuario que ingrese un numero_usuario
numero_usuario:int=int(input("ingrese un numero que sea entre 1- 9: "))
#multiplicamos el numero_usuario en si mismo *9
numero_usuario=numero_usuario*9
#multiplicamos el numero_magico por el numero_usuario en si mismo
numero_magico=numero_usuario*numero_magico
#imprimimos el numero_magico
print(numero_magico)

### EJERCICIOS 2
## 1
#comparar dos edades ingresados por el usuario y determinar si son iguales o diferentes
edad1:int=int(input("ingrese la primera edad: "))
edad2:int=int(input("ingrese la segunda edad: "))
diferencia:bool=edad1!=edad2 
comparacion=diferencia==0
print(comparacion)

## 2
#determinar si un año ingresado por el usuario es anterior al año actual
año_ingresado:int=int(input("ingrese un año: "))
comparacion:bool=año_ingresado<2024
print(comparacion)

## 3
#valiar si un numero ingresado por el usuario es positivo, negativo o cero
numero:int=int(input("ingrese un numero: "))
positivo:bool=numero<0 
negativo:bool=numero>0
cero:bool=numero==0
print(positivo)
print(negativo)
print(cero)

## 4
#validar si un numero ingresado por el usuario es primo o no 
numero_ingresado:int=int(input("ingresa un numero entero: "))
comparacion=numero_ingresado%2!=0 
print(comparacion)

## 5
#determinar si un numero ingresado por el usuario es par y mayor que 10
numero_ingresado:int=int(input("ingrese un numero: "))
resto=numero_ingresado%2
determinar:bool=resto==0 and numero_ingresado >10
print(determinar)