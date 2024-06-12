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