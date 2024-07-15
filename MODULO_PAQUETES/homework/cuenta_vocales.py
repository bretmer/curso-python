"""modulo para contar vocales"""
def f_cuenta_vocales(texto:str):
    """funcion para contar la cantidades de vocales a aparecen en un texto"""
    texto_minuscula:str=texto.lower()
    cantidad_vocales=0
    for n in texto_minuscula:
        if n == "a":
            cantidad_vocales+=1
    return cantidad_vocales
