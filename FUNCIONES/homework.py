# crear una funcion que reciba por argumento n numeros y retorne una lista con los numeros pares
def numeros_pares(*args):
    return [n for n in args if n %2==0]
print(numeros_pares(4,5,6,7,8,9,12,10))


# crear tres funciones para los siguientes casos
# calcular el numero menor
# calcular el numero mayor
# calcular la suma de todos los numeros
# se le pasara por aargumentos n numeros
def menor(*args):
    menor=args[0]
    for n in args:
        if n<menor:
            menor=n
    return menor
def mayor(*args):
    mayor=args[0]
    for n in args:
        if n>mayor:
            mayor=n
    return mayor
def suma(*args):
    for n in args:
        suma+=n
    return suma
numeros=2,4,6,8,9,2,3
print(menor(*numeros))
print(mayor(*numeros))
print(suma(*numeros))
