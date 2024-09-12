import inspect
import os
import shutil
from pathlib import Path
from typing import *  # noqa: F403


def logger(type, message):
    if type == "error":
        return print(f"|❌ {message}")
    if type == "warning":
        return print(f"|⚠️ {message}")


def clean() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def rolback(route: Path):
    inspect.stack()[2](route)


def middleware(func: Callable) -> Callable:  # noqa: F405
    def wrapper(*args, **kwargs) -> str:
        # code before input call
        result = func(*args, **kwargs)
        # code after input call
        clean()
        return result
    return wrapper


input = middleware(input)


def countRecipe(route: Path) -> int:
    return len(list(route.glob("**/*.txt")))


def masthead(route: Path):
    print("-" * 20)
    text = "Recetario: "
    print(f"| {text:^17} |")
    print("-" * 20)
    totalrecipe = countRecipe(route)
    print(
        f'''
    🛣️: {route}
    La cantidad de recetas en el sistema: {totalrecipe}
    ''')


def printPathNames(route: Path, isDir: bool = True):
    for i, element in enumerate(route.iterdir()):
        if element.is_dir() and isDir:
            print(f'{i+1}: {element.name}')
        else:
            print(f'{i+1}: {element.stem}')


def readRecipe(route: Path):
    printPathNames(route)
    index = int(input("Escoge una Categoria: "))
    if index == len(list(route.iterdir())):
        rolback(route)

    category = list(route.iterdir())[index - 1]

    if countRecipe(category) == 0:
        print("La categoria no tiene archivos para leer")
        input()
        return
    print(
        f"La categoria {category.name} tiene {countRecipe(category)} recetas")
    printPathNames(category)
    recipe = int(input("Cual te gustaria leer: ")) - 1
    print(list(category.glob("*.txt"))[recipe].read_text(encoding='utf-8'))
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


def createCategory(route: Path):
    nameCategory = input("Digite el nombre de la nueva categoria: ")
    Path(route / nameCategory).mkdir()
    print("🥳 La categoria fue escrito con exito ")
    input()


def deleteRecipe(route: Path):
    printPathNames(route)
    category = int(input("Escoge una Categoria: ")) - 1
    print(
        f"La categoria {list(route.iterdir())[category].name} tiene {countRecipe(list(route.iterdir())[category])} recetas")
    printPathNames(list(route.iterdir())[category])
    recipe = int(input("Cual te gustaria eliminar: ")) - 1
    file_path = list(list(route.iterdir())[
        category].glob("*.txt"))[recipe]
    file_path.unlink()
    print(f"El archivo '{file_path}' ha sido eliminado.")
    input()


def deleteCategory(route: Path):
    printPathNames(route)
    category = int(input("Escoge una Categoria: ")) - 1
    file_in_category = len(list(list(route.iterdir())[category].glob("*.txt")))
    if file_in_category > 0:
        yes_or_no = input(
            f"Esta categoria tiene {file_in_category} recetas asociadas, quieres eliminarla yes/no: ")
        if yes_or_no == "yes":
            shutil.rmtree(list(route.iterdir())[category])
    else:
        list(route.iterdir())[category].rmdir()

    print(f"La categoria {list(route.iterdir())[category]} fue eliminada")
    input()


def getMenu():
    return '''
    1: Leer Receta
    2: Crear Receta
    3: Crear Categoria
    4: Eliminar Receta
    5: Eliminar Categoria
    6: Salir
    '''


menu = [readRecipe, createRecipe, createCategory, deleteRecipe, deleteCategory]


def main():
    while True:
        route = Path(Path(__file__).parent / "Recetas")
        masthead(route)
        try:
            userChoose = int(input(getMenu()))
            if userChoose == 6:
                break
            menu[userChoose - 1](route)
        except IndexError:
            logger("error", "No existe esa opcion, por favor escoge una valida")
        except ValueError:
            logger("error", "Por favor, escribe solo numeros")


if __name__ == "__main__":
    clean()  # Clear the current console
    main()  # Enter door
    os.system("exit")
