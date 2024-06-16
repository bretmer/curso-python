# FUNCIONES
Matematicamente una funcion es una operacion que toma uno o mas valores llamados `argumentos` y produce un valor denominado `resultado` .
> [!NOTE]
>Todos los lenguajes de programacion tienen funciones incorporadas `(funciones internas)`, y funciones creadas por el usuario `(funciones externas)`.
En programacion una funcion es un subprograma, es una estructura que nos permite agrupar codigos y sus principales objetivos son:
- `NO REPERTIR` fragmentos de codigo
- `REUTILIZAR` el codigo de distintos escenarios
## ESTRUCTURA DE UNA FUNCION
Una funcion viene `definida` por un `nombre`, sus `parametros` y su valor `retorno`.
una vez creada la funcion podremos solicitar su ejecucion `invocando` la funcion por su `nombre`. 
## DEFINIR UNA FUNCION EN PYTHON
Para definir una funcion en python primero utilizaremos la palabra reservada `def` seguida por el `nombre` de la funcion. A continuacion especificaremos `los parametros○`, con `()` si es una funcion sin parametros, `(a)` si es una funcion con parametros, si se tuviere mas de un parametro iran separadas por `,`, finalizaremos la linea con `:` en la siguiente linea sin olvidar el identado, comenzara el `cuerpo` de la funcion (microprograma) que puede contener uno o mas sentencias, finalmente debera `retornar` un resultado con la palabra reservada `return`.
> [!TIP]
> Como retorno tambien se ouede utilizar la `funcion interna` , `print`, para depuracion de codigo no es recomendable usarlo en produccion. 
> 
> print dentro de una funcion es una herramienta que nos permite comprobar que una funcion este haciendo el trabajo de manera corrcta.
**Ejemplo:**
```python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    return saludo+saludo_dos 
    # iterable f"{saludo}, {saludo_dos}"
    # print(f"{saludo}, {saludo_dos}")
print(saludo())
# saludo()
```
## INVOCAR UNA FUNCION 
Para invocar, o llamar una funcion solo tendremos que escribir el `nombre` de la funcion seguido por `()` parentesis
```python
def saludo():
    print("hola")
# invocamos la funcion
saludo()
```
## RETORNAR UN VALOR
Las funciones pueden retornar (o devolver) un valor
```python
def uno():
    return 1
uno()
```
>[!WARNING]
No confundir `print()` com `return`, el valor retornado por `return` nos permite usar fuera de su contexto. y `print()` solo mostrara el literal por terminal.
## RETORNANDO MULTIPLES VALORES
El secreto es hacerlo mediante un tipo de datos estructurados
```python
def tupla():
    return 2,3,4
varios()
#retorna(2,3,4)
def lista():
    return ["hola",45]
lista()
#retorna["hola",45]
def dicc():
    return {"nombre":"jose","edad":45}
dicc()
#retorna {"nombre":"jose","edad":45}
```
## PARAMETROS Y ARGUMENTOS
Si una funcion no dispusioera de valores de entrada estaria limitada en su actuacion. es por ello que los `parametros` nos permite variar los datos que consumen una funcion para obetener distintos resultados.

**ejemplo**
*crear una funcion que reciba u valor numerico y devuelve su raiz cuadrada* 
```python
def sqrt(valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es el argumento de la funcion
sqrt(4)
```
Cuando llamemos a una funcion con `argumentos`, los valores de estos argumentos se copian en los valores correspondientes `parametros` dentro de la funcion.
```python
def ejem(a,b,c):
    return (a+b+c)
ejem(4,5,6)
```
### ARGUMENTOS NOMINALES
En esta argumentacion los argumentos no son copiados en un orden especifico sino que **se asignan por nombre a cada parametro**. Ello nos permite evitar el problema de conocer o recordar cual es el orden de los parametros en la definicion de la funcion. Para utilizarlo, basta con realizar una asignacion de cada argumento en la propia llamada de la funcion.

**Ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
        la cpu es de la familia {familia},
        con {num_core} cores y con una 
        frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos nominales
build_cpu(num_core=4,familia="intel",frecuncia=2.7)
```
### ARGUMENTOS POSICIONALES
Los argumentos son copiados en un orden especifico, en este caso debemos conocer o recordar cual es el orden de los parametros.

**Ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
        la cpu es de la familia {familia},
        con {num_core} cores y con una 
        frecuencia de {frecuencia}
    """)
# haciendo uso de los argumentos posicionales
build_cpu("intel",4,2.7)
```
## PARAMETROS POR DEFECTO
Es posible especificar **valores por defecto** en los parametros de una funcion, en el caso de que no se proporcione una valor al argumento en la llamada a la funcion, el parametro correspondiente tomara el valor definido por defecto.

**Ejemplo**
```python
def alumnos(nombre,apellido,estado="aprobado")

alumnos("ruth","castillo")
alumnos("anthony","cruzes","desaprobado")
```
## DESEMPAQUETADO/EMPAQUETADO DE ARGUMENTOS
Python nos ofrece la posibilidad de empaquetar y desempaquetar argumentos cuando estamos invocando a una función, tanto para `argumentos posicionales` como para `argumentos nominales`. Y de esto se deriva el hecho de que podamos utilizar un número variable de argumentos en una función, algo que puede ser muy interesante según el caso de uso que tengamos.
### EMPAQUETADO/DESEMPAQUETADO DE ARGUMENTOS POSICIONALES
El empaquetado y desempaquetado de argumentos posicionales es una característica poderosa que permite manejar múltiples argumentos de manera flexible y concisa. A continuación, se explica cómo funciona este proceso con ejemplos detallados.
- **EMPAQUETAR ARGUMENTOS POSICIONALES :** 👍Si utilizamos el operador `*` delante del nombre de un parámetro posicional, estaremos indicando que los argumentos pasados a la función se empaqueten en una tupla.
>**Ejemplo**
```python
def sumar(*numero):
    return sum(numero)
print(sumar(1, 2, 3))    #la salida es 6
```
-  **DESEMPAQUETAR ARGUMENTOS POSICIONALES :** 👍El desempaquetado de argumentos posicionales es cuando se llama a una función. Esto se logra utilizando el operador `*` al pasar los argumentos.
```python
def multiplicar(a, b, c):
    return a * b * c
valores = (2, 3, 4)
resultado = multiplicar(*valores)
print(resultado)  # el resultado es 24
```
### EMPAQUETADO/DESEMPAQUETADO DE ARGUMENTOS NOMILALES
el empaquetado y desempaquetado de argumentos nominales es una característica que permite trabajar con funciones que aceptan un número variable de argumentos con nombre. Este proceso se realiza utilizando el operador `**` .
- **EMPAQUETADO DE ARGUMENTOS NOMILAES :** 👍Cuando usamos el operador `**` delante del nombre de un parámetro con nombre en una función, estamos señalando que los argumentos pasados a la función como pares `clave-valor` se agruparán en un diccionario.
>**Ejemplo:**
```python
def mostrar_informacion(**registro):
    for clave, valor in registro.items():
        print(f"{clave}: {valor}")
mostrar_informacion(nombre="Juan", edad=30, ciudad="Madrid") 
```
- **DESEMPAQUETADO DE ARGUMENTOS NOMILAES :** 👍El desempaquetado de argumentos nominales se realiza utilizando `**` cuando se llama a una función. Esto permite pasar un diccionario de argumentos a una función como si fueran argumentos con nombre individuales.
>**Ejemplo:**
```python
def imprimir_detalles(nombre, edad, ciudad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
detalles = {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"}
imprimir_detalles(**detalles)
```
## FUNCIONES INTERNAS DE PYTHON
### FUNCION DE CONVERSION
- `int():` Convierte un valor a un número entero.

```python
num = int("123")
print(num)  # 123
```
- `float():` Convierte un valor a un número de punto flotante.
```python
num = float("123.45")
print(num)  # 123.45
```
- `str():` Convierte un valor a una cadena de texto.
```python
texto = str(123)
print(texto)  # '123'
```
- `bool():` Convierte un valor a un booleano (True o False).
```python
booleano = bool(1)
print(booleano)  # True
```
### FUNCION PARA EL MANEJO DE COLECCIONES
- `len():` Devuelve la longitud de una colección.
```python
longitud = len([1, 2, 3])
print(longitud)  # : 3
```
- `max():` Devuelve el valor máximo de una colección.
```python
maximo = max([1, 2, 3])
print(maximo)  # : 3
```
- `min():` Devuelve el valor mínimo de una colección.
```python
minimo = min([1, 2, 3])
print(minimo)  # : 1
```
- `sum():` Devuelve la suma de una colección de números.
```python
suma = sum([1, 2, 3])
print(suma)  # : 6
```
- `sorted():` Devuelve una lista ordenada a partir de una colección.
```python
ordenada = sorted([3, 1, 2])
print(ordenada)  # : [1, 2, 3]
```
- `enumerate():` Devuelve un objeto enumerado (índice, valor) a partir de una colección.
```python
lista = ['a', 'b', 'c']
for indice, valor in enumerate(lista):
    print(indice, valor) #0 a  #1 b  #2 c
```
- `zip():` Combina varias colecciones en una sola.
```python
nombres = ['Ana', 'Luis']
edades = [25, 30]
combinados = zip(nombres, edades)
print(list(combinados))  # : [('Ana', 25), ('Luis', 30)]
```
### FUNCION PARA LA MANIPULACION DE CADENAS
- `len():` Devuelve la longitud de una cadena.
```python
cadena = "Hola, mundo!"
longitud = len(cadena)
print(longitud)  # 12
```
- `split():` Divide la cadena en una lista de subcadenas basadas en un delimitador.
```python
texto = "uno, dos, tres"
lista = texto.split(", ")
print(lista)  # ['uno', 'dos', 'tres']
```
- `join():` Une una lista de cadenas en una sola cadena, utilizando un delimitador.
```python
lista = ["uno", "dos", "tres"]
unido = ", ".join(lista)
print(unido)  # 'uno, dos, tres'
```
### FUNCIONES DE ENTRADA/SALIDA
- `print():` Imprime un valor en la salida estándar.
```python
print("Hola, mundo!")  # Hola, mundo!
```
- `input():` Lee una cadena desde la entrada estándar.
```python
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}!")
```