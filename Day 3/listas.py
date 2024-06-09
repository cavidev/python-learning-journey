mi_lista = ["a", "b", "c"]

print(type("mi_lista"))

# puede manejar varios tipos de datos
otra_lista = ["hola", 55, 6.1]

# Se puede saber el largo de las listas
print(len(mi_lista))

# NOTA: todos los metodos de string tambien los ejecuta las listas
desde = 1
hasta = 4
saltando = 2
resultado = mi_lista[desde:hasta:saltando]
print(resultado)

#las listas si se puede sobreescribir los elementos
mi_lista[1] = "👾"
print(mi_lista)

# Se puede eliminar con metodos 
eliminado = mi_lista.pop(1)
print(eliminado)
print(mi_lista)

# Se puede ordenar las listas
lista = ["z", "j", "a", "b", "w"]
lista.sort()
print(lista)


lista.reverse()
print(lista)

lista.append