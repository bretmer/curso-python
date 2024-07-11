# MODULOS Y PAQUETES EN PYTHON
## MODULO
>[!TIP]
Es un archivo de Python cuyos objetos **(funciones, clases, excepciones, etc.)** pueden ser accedidos desde otro archivo, se trata simplemente de una forma de organizar grandes códigos. El nombre de archivo es el nombre del módulo con el sufijo **`.py`** agregado.

**Ejemplo:** 
>Por ejemplo, un archivo `aritmetica.py` que contenga las siguientes definiciones.
```python
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def producto(a, b):
    return a * b

def divición(a, b):
    return a / b
```
>Podemos acceder a ellas desde otro archivo de Python ubicado en la misma ruta importando el módulo.
```python
import aritmetica
print(aritmetica.sumar(7, 5))
```
>Tambien se puede importar objetos desde un módulo con la siguiente sintaxis.
```python
from aritmetica import sumar
print(sumar(7, 5))
```
>Podemos importar varios objetos separándolos por comas.
```python
from aritmetica import suma, resta, producto, divición
print(suma(7, 5))
print(resta(7, 5))
print(producto(7, 5))
print(divición(7, 5))
#O tambien, para importar todos los objetos dentro de un módulo se utiliza el *
from aritmetica import *
```
>[!TIP]PAQUETES
 Es una carpeta que contiene varios módulos. Debe contener siempre un archivo `__init__.py` para que Python entienda que se trata de un paquete y no de una simple carpeta.

**Ejemplo:**
```
matematica/
    | __init__.py
    | aritmetica.py
    | geometria.py
```
>Así, podemos acceder a alguno de los módulos del paquete de la siguiente manera.
```python
import matematica.aritmetica
print(matematica.aritmetica.suma(7, 5))
```
O bien de la siguiente:
```python
from matematica import aritmetica
print(aritmetica.suma(7, 5))
```
También, esta otra:
```python
from matematica.aritmetica import suma
print(suma(7, 5))
```
## DIFERENCIAS ENTRE MODULO Y PAQUETES
- **Paquetes:** Es una carpeta con una serie de archivos `.py`. Es una colección de módulos organizados en una directorio con un archivo `__init__.py` en su interior lo cual se utiliza para organizar varios módulos en una estructura de directorios, que es especialmente útil en proyectos grandes.

- **Modulos:** Es un conjunto de funciones `.py` que permite a los módulos organizar y reutilizar el código. Se puede importar un módulo a otro programa para usar sus funciones y clases.