# EJERCICIOS

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no
edad_usuraio:int=int(input("ingrese su edad: "))
if edad_usuraio >=18:print("ya eres mayor de edad")
else:print("eres menor de edad")


# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña
# e imprima por pantalla si la contraseña introducida por el usuario coincide con la  guardada en la variable sin tener en cuenta 
# mayusculas y minusculas
codigo_binario=0
contraseña:str="silvestre"
password:str=input("ingrese una contraseña: ")
if contraseña == password:print("la contraseña ingresada coincide") 
else:print("la contraseña ingresada es incorrecta")


# Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero 
# hasta cero separados por coma
positivo=""
numero:int=int(input("ingrese un numero: "))
for i in range(numero,-1,-1):
    positivo += str(i)
    if i > 0:
        positivo +=","
print(positivo)