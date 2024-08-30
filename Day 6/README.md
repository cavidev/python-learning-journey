# Day 5

## Files

```python
# Open the file, needs be in the seme directory
my_file = open("test.txt")

# read and print the file content
print(my_file.read())

# close the file
my_file.close()
```

```python
# You can read the file as a list
my_file = open("test.txt")

my_list_file = my_file.readlines()

print(my_list_file[1])
```

```python
'''
Mode to open
r = read (Default)
w = write (reset the file)
a = only write (in the final of the list) 
'''
# my_file = open("text.txt", <mode>)

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
 
registro = open("registro.txt","a")
for item in registro_ultima_sesion:
    registro.writelines(item +'\t')
 
registro.close()
registro = open("registro.txt","r")
print(registro.read())

```

## Directory
### Read the own path
```python
import os
path = os.getcwd()
print(path)

```

### Read other path
```python 
import os

path = os.getcwd()
os.chdir("D:\\Documents\\Playground\\python-learning-journey\\Day 6 New Routes")

file = open("otherFile.txt")

print(file.read())
```

## Path lib
```python
from pathlib import Path

guia = Path("Barcelona", "Sagrada_Familia")
print(guia)

```
