import os
from pathlib import Path
import sys


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def middleware(func):
    def wrapper(*args, **kwargs):
        # code before input call
        resultado = func(*args, **kwargs)
        # code after input call
        clean()
        return resultado
    return wrapper


input = middleware(input)


def countRecipe(route: Path):
    return len(list(route.glob("**/*.txt")))


def printMenu():
    return '''
    1: Leer Receta
    2: Crear Receta
    '''


def masthead():
    print("-" * 20)
    text = "Recetas: "
    print(f"| {text:^17} |")
    print("-" * 20)


def printPathNames(route: Path, isDir: bool = True):
    for i, element in enumerate(route.iterdir()):
        if element.is_dir() and isDir:
            print(f'{i+1}: {element.name}')
        else:
            print(f'{i+1}: {element.stem}')


def readRecipe(route: Path):
    printPathNames(route)
    category = int(input("Escoge una Categoria: ")) - 1
    print(
        f"La categoria {list(route.iterdir())[category].name} tiene {countRecipe(list(route.iterdir())[category])} recetas")
    printPathNames(list(route.iterdir())[category])
    recipe = int(input("Cual te gustaria leer: ")) - 1
    print(list(list(route.iterdir())[
          category].glob("*.txt"))[recipe].read_text(encoding='utf-8'))
    input()


def createRecipe(route: Path):
    printPathNames(route, True)
    category = int(input("Donde deseas crear la nueva receta: ")) - 1
    name = input("Escribe el nombre de la receta: ")
    content = input("Escribe la receta: ")
    new_file = Path(list(route.iterdir())[category] / f"{name}.txt")
    new_file.write_text(content, encoding='utf-8')
    print("🥳 El archivo fue escrito con exito ")
    input()


def main():
    while True:
        masthead()
        route = Path(Path(__file__).parent / "Recetas")
        totalrecipe = countRecipe(route)
        print(
            f'''
        🛣️: {route}
        La cantidad de recetas en el sistema: {totalrecipe}
        ''')
        userChoose = input(printMenu())
        def method(a): return print("No Escogido")
        if (userChoose == "1"):
            method = readRecipe
        if (userChoose == "2"):
            method = createRecipe
        if (userChoose == "6"):
            # sys.exit("Finalizando la ejecución")
            break
        method(route)


if __name__ == "__main__":
    clean()
    main()
