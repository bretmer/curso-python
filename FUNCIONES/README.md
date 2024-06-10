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
