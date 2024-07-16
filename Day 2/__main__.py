# Calculadora de comisiones
def main():
    nombre = input("Cual es tu nombre: ")
    cantidadVendida = int(input("Cuanto has vendido: "))
    # Extra: con una funcion

    def sacarComisiones(cantidadVendida):
        return round((cantidadVendida*13)/100, 2)
    print(
        f"Hola {nombre} tus ganacias por comiciones son: {sacarComisiones(cantidadVendida)} $")


if __name__ == "__main__":
    main()
