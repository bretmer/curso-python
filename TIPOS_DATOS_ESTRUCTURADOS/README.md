# TIPOS DE DATOS ESTRUCTURADOS (TDA - Tipos de datos abstractos)
```python
# lista : sus valores o elementos se puede actualizar, eliminar.
lista=["abel",20,5.2,5,False,["texto",.2]]

# tuplas : sus valores o elementos no pueden ser modificdos o eliminados.
tupla=("abel",20,5.2,5,False,[])

# diccionario u objeto :
# los diccionario almacenan los datos con clave:valor 
diccionario={"nombre":"antonio","edad":15,"sexo":False}
```
- [!TIP]
- **observacion:** que los tipos de datos estrucuturdos pueden almacenar en su interior otros tipos de datos estructurados.

```python
lista_alumnos={
    {
        "nombre":"abel",
        "edad":20,
        "amigos":["no tiene"]
    },{
        "nombre":"ruth",
        "edad":13,
        "amigos":["flor","rocio"]
    },{
        "nombre":"jose ma,
        "edad":80
    },{
        "nombre":"ronny",
        "edad":15
    }
}
```
## METODOS
### 1. convertir texto a lista
```python
# Metodo list
texto="hola"
list(texto) #["h","o","l","a"]

# Metodo split
texto="hola como estan alumnitos lindos"
texto.split(" ")
```
### 2. Agregar elementos a una lista
```python
# Metodo append :
#  agrega al final de la lista
lista=["hola"]
lista.append("mundo")
print(lista)

# Metodo insert :
# permite agregar elementos en cualquier ubicacion de mi  lista
lista_nombres=["edith", "ruth","luz"]
lista_nombres.insert(0,"antony")
```
### 3. Eliminar elementos de una lista
```python
# Metodo pop :
# elimina el ultimo elemento de una lista
lista_nombres=["edith", "ruth","luz"]
lista_nombres.pop()

# Metodo remove :
# elimina el nombre que coincida dentro de mi lista.
lista_nombres=["edith", "ruth","luz"]
lista_nombre.remove("ruth")

# Metodo pop : 
# al pasarle por parametro un indice este lo eliminara de la lista.
lista_nombres=["edith", "ruth","luz"]
lista_nombres.pop(0)
```
### 4. Buscar un elemento en una lista
```python
lista_nombres=["edith", "ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombres[indice])

pertenencia="edith" in lista_nombres #True . False
```
### 5. Comparacion de listas
podemos hacer uso de los operadores de comparacion para comparar listas.
**Ejemplo:**
```python
comparar=[1,2,3]>[1,2,4]
print(comparar)  # False
```
### 6. Cuidado con las copias

### 7. Fe de erratas (actualizar listas)
```python
lista=[1,3,4,5,6]
lista[0]=2
print(lista)  # lista actualizada [2,3,4,5,6]

# modificando lista con diccionario
alumnos=[
    {
        "nombres":"abel",
        "edad":15
    },
    {
        "nombre":"antony",
        "edad":29
    }
]
alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15}
alumnos[1]["sexo"]="por definir"
print(alumnos)
```