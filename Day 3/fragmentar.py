#SLICING
texto = "ABCDEFGHIJKLM"

fragmento = texto[2]
print(fragmento)

# Recorre desde 2 hasta (sin incluirlo)
fragmento = texto[2:5]
print(fragmento) #>> CED

# Si se omite el ul ultimo factor
fragmento = texto[2:]
print(fragmento) #>> CEDFGHIJKLM

# Si se hace al revez, desde el comienzo hasta el 5 (sin incluirlo)
fragmento = texto[:5]
print(fragmento) #>> ABCDE

# Con un tercer parametro, salta los caracteres
fragmento = texto[2:10:2]
print(fragmento) #>> CEGI

# Si solo ponemos el tercer parametro, va saltando de 2 en 2
fragmento = texto[::2]
print(fragmento) #>> ACEGIKM

# Si ponemps un -1 negativo, le da la vuelta al string 
fragmento = texto[::-1]
print(fragmento) #>> MLKJIHGFEDCBA

# con otros numeros, los salta.
