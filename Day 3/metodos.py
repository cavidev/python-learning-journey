texto = "Este es el texto de Carlos"

# Trasformar todas las letras en mayuscula
resultado = texto.upper();
print(resultado) #>> ESTE ES EL TEXTO DE CARLOS

# Se puede seleccionar solo un indice que le aplique la operacion
resultado = texto[2].upper();
print(resultado)#>> T

# Se puede usar el de misnuscular
resultado = texto[2].lower();
print(resultado) #>> t

# Con el metodo de split se puede trasformat en listas
resultado = texto.split();
print(resultado) #> ['Este', 'es', 'el', 'texto', 'de', 'Carlos'] 

# se puede poner un caracter como un separador
resultado = texto.split("t");
print(resultado) #> ['Es', 'e es el ', 'ex', 'o de Carlos']

# Con el metodo join, uno las string
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e) #> Aprender Python es genial

#Con el metodo replace, reemplaza el string especificado
resultado = texto.replace("e", "🚀" )
print(resultado) #>> Est🚀 🚀s 🚀l t🚀xto d🚀 Carlos

