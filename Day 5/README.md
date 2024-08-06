# Day 5

## Search information about the methods in the Python Doc

[.lstrip Method](https://docs.python.org/es/3/library/stdtypes.html#str.lstrip)

```py
string = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(string.lstrip(",:%_#T"))
```

[.insert Method](https://docs.python.org/es/3/library/array.html#array.array.insert)
```py
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
```

[.isdisjoint Method](https://docs.python.org/es/3/library/stdtypes.html#frozenset.isdisjoint)
```py
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)
```

## Function

### Function Body
```py
def saludar():
    print("¡Hola mundo!")
```

```py
def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")
```

```py
un_numero=2
def cuadrado(un_numero):
    print(un_numero**2)
```

### Function Return

```py
def potencia(numero, exponente):
    return numero**exponente
```

```py
dolares = 2
def usd_a_eur(usd):
    return usd*0.90
```

```py
palabra="Python"
def invertir_palabra(palabra):
    return palabra[::-1].upper()
```

### Function Dinamic 
```py
lista_numeros = [1,2,3,4,5,6,7,8,9]
def todos_positivos(lista_numeros ):
    for n in lista_numeros:
        if n < 0:
            return False
    return True
```

```py
lista_numeros=[1,2,4,4000]
def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0 and n < 1000:
            suma = suma + n
    return suma
```

### Function interaction

```py
from random import randint
def lanzar_dados():
    return (randint(1,7), randint(1,7))
    
def evaluar_jugada(args):
    suma_dados = sum(args)
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
```

```py
from random import choice

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def lanzar_moneda():
    return choice(["Cara", "Cruz"])


def probar_suerte(resultado, lista_numeros):
    if resultado == "Cara":
        print("La lista se autodestruirá")
        lista_numeros = []
        return lista_numeros
    else:
        print("La lista fue salvada")
        return lista_numeros


print(probar_suerte("Cara", lista_numeros))
```

### Function with undefined arguments (*args)

```py
def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg**2
    return suma
```

```py
def suma_absolutos(*args):
    suma = 0
    for arg in args:
        # <absolute number>
        suma += abs(args)
    return suma
```

### Function with undefined arguments(**kwargs)
```py
def cantidad_atributos(**kwargs):
    return len(kwargs)
```

```py
def lista_atributos(**kwargs):
    return list(kwargs.values())
```

```py
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for (nombre_argumento, valor_argumento) in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")
```