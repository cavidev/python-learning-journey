
# Se puede correr un string por medio de los indices
mi_texto = "Esto es una prueba"
resultado = mi_texto[0] # E
print(resultado) #>> E

# Python puede recorrer de derecha a izquierda con los negativos
resultado = mi_texto[-4];
print(resultado) #>> u

# Se puede buscar un indice por la letra que queremos
resultado = mi_texto.index("n");
print(resultado) #>> 9

# Tambien funciona con palabras completas
resultado = mi_texto.index("prueba");
print(resultado) #>> 12

# Se puede decirle desde donde empezar a busvar
resultado = mi_texto.index("a", 5);
print(resultado) #>> 10

# y hasta donde parar la busqueda
resultado = mi_texto.index("a", 5, 11);
print(resultado) #>> 10

# se puede buscar de derecha a izquierda 
resultado = mi_texto.rindex("a", 5, 11);
print(resultado) #>> 10

