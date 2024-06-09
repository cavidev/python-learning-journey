# Los string son inmutables, igual que en javascript
nombre = "Iancy"
# nombre[0] = "Y"

# Se puede multiplicar los string con las operaciones matematicas
n1 = "Carlos"
n2 = n1 * 5
print(n2)

# Se puede manejar los string con las tres comillas
poema = """Mil pequeños peces blancos
comosi hirviera
el color del agua
"""
print(poema)

# Para saber si agua esta en poema
print("agua" in poema)

# O con la negacion
print("sol" not in poema)

# Se puede obtener el largo de u string
print(len(poema))
