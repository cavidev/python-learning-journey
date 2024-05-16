# Conversiones implicitas
# Python lee las variables y las convierte por si solo
num1 = 20
num2 = 30.5

convertido = num1 + num2
print(type(convertido))# <class float>
#Aqui se convirtio la variable a float

# Conversiones explicitas
num1 = 5.8
print(type(num1))# <class float>

print(type(int(num1)))# <class int>

# Pidiendo datos al usuario y convirtiendolas en int
edad = input("Dame tu edad") 
print(type(edad))# <class string>

edad = int(edad) # Lo convertidos a int
print(type(edad))# <class int>

#Práctica con Conversiones 1
# Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:
num1 = 7.5
print(type(int(num1)))

# Práctica con Conversiones 2
# Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:

num2 = 10
print(type(float(num2)))