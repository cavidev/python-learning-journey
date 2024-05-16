x = 10
y = 5

# La opcion numero uno es com format
print("Mis numero son {} y {}".format(x,y))

# O con la opcion cadela literal 
print(f"Mis numero son {x} y {y} y el resultado es {x+y}")


# Práctica Formatear Cadenas 1
# Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:
# Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)
# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.

nombre_asociado = "Carlos"
numero_asociado = 2222222
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")


# Práctica Formatear Cadenas 2
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:
# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
# Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto

puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")