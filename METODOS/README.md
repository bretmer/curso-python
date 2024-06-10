# Metodos de python
## NUMEROS
```python
len(154789)
# devuelve la cantiadad de digitos
# 6
```
## TEXTO
```python
len("hola mundo")
# devuelve la cantidad de caracteres
# el espacio cuenta tambien como un caracter
# 10
```
1. str.lower(): Convierte todas las letras de la cadena a minúsculas.
```python
"HELLO".lower()  # 'hello'
``` 
2. str.upper(): Convierte todas las letras de la cadena a mayúsculas.
```python
"hello".upper()  # 'HELLO'
```
3. str.strip(): Elimina los espacios en blanco al principio y al final de la cadena.
```python
"  hello  ".strip()  # 'hello'
```   
4. str.replace(old, new): Reemplaza todas las apariciones de una subcadena por otra.
```python
"hello world".replace("world", "Python")  # 'hello Python'
```

5. str.split(sep=None): Divide la cadena en una lista usando un separador específico (por defecto, cualquier espacio en blanco).
```python
"hello world".split()  # ['hello', 'world']
```
## LISTAS  
1. list.append(x): Añade un elemento al final de la lista.
```python
my_list = [1, 2, 3]
my_list.append(4)  # [1, 2, 3, 4]
```
       
2. list.extend(iterable): Extiende la lista añadiendo todos los elementos de un iterable.
```python
my_list = [1, 2, 3]
my_list.extend([4, 5])  # [1, 2, 3, 4, 5]
``` 
3. list.insert(i, x): Inserta un elemento en una posición específica.
```python
my_list = [1, 2, 3]
my_list.insert(1, 'a')  # [1, 'a', 2, 3]
```      
4. list.remove(x): Elimina la primera aparición de un valor.
```python
my_list = [1, 2, 3, 2]
my_list.remove(2)  # [1, 3, 2]
```      

5. list.pop([i]): Elimina y devuelve el elemento en la posición indicada (por defecto, el último).
```python
my_list = [1, 2, 3]
my_list.pop()  # 3, my_list es ahora [1, 2]
```      
## TUPLAS
Las tuplas son inmutables, así que no tienen métodos para modificar su contenido, pero puedes usar métodos comunes para inspeccionarlas:

1. tuple.count(x): Devuelve el número de veces que un valor aparece en la tupla.
```python
my_tuple = (1, 2, 2, 3)
my_tuple.count(2)  # 2
```   
   
2. tuple.index(x[, start[, end]]): Devuelve el índice de la primera aparición de un valor.
```python
my_tuple = (1, 2, 3)
my_tuple.index(2)  # 1
```      
## DICCIONARIO
1. dict.get(key[, default]): Devuelve el valor para una clave, o un valor por defecto si la clave no existe.
```python
my_dict = {"a": 1, "b": 2}
my_dict.get("a")  # 1
my_dict.get("c", 0)  # 0
```       
2. dict.keys(): Devuelve una vista de todas las claves en el diccionario.
```python
my_dict = {"a": 1, "b": 2}
my_dict.keys()  # dict_keys(['a', 'b'])
```    
3. dict.values(): Devuelve una vista de todos los valores en el diccionario.
```python
my_dict = {"a": 1, "b": 2}
my_dict.values()  # dict_values([1, 2])
```      
4. dict.items(): Devuelve una vista de los pares clave-valor en el diccionario.
```python
my_dict = {"a": 1, "b": 2}
my_dict.items()  # dict_items([('a', 1), ('b', 2)])
```    
5. dict.update([other]): Actualiza el diccionario con los pares clave-valor de otro diccionario u iterable de pares clave-valor.
```python
my_dict = {"a": 1}
my_dict.update({"b": 2, "c": 3})  # {"a": 1, "b": 2, "c": 3}
```

