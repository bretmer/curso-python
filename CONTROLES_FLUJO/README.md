# CONTROLES DE FLUJO
todos los programas trabajan de atraves de instrucciones ordenadas.
existen maneras de romper el flujo normal de los programas
creando `bifurcaciones` o creando `repeticion` de instrucciones.
## DECISIONES
### La sentencia if
la sentencia de decision en python es `if` .en su estructura debemos añadir una **expresion de comparacion** terminando con `:` al final de la lista
> ejemplo:

```python
if True:
    print("es verdad")
```
## CICLOS
son los controles de flujo que repiten codigo y su sintaxsis es la siguiente
### for
> Para for:
```python
# este codigo imprime los numeros del 1 al 10
for n in range(1,11):
    print(n)
```
#### `range`
consume menos memoria y es mas rapida en oraciones pequeñas
#### `in`
consume menos memoria y es mas rapida en oraciones medianas
#### `enumerate`
consume mas memoria y es mas rapida con oraciones medianas y oraciones mas largas

### while
es un mecanismo que usa `python` para repetir instrucciones, la semantica de esta sentencia es: `Mientras se cumpla la condicion has algo`
```python
while True:
    print("hola")
# es un bucle infinito

# METODOS DE STRING = ARRAY
nombre="jose"
nombre.upper() #convirete el texto a mausculas

apellidos="ALVAREZ"
apellidos.lower() #convirete el texto a minusculas

segundo_nombre="luis"
segundo_nombre.capitalize() #convierte la primera letra en mayuscula
```
