# Inicio

### Metodo `os.path.join()`

El metodo `join()` de `os.path` es una herramienta muy util para manipular archivos en python.
Su **principal función** es concatenar *(unir)* uno o más componentes de una ruta, creando una ruta completa y válida para el sistema operativo en el que se está ejecutando el condigo.

#### Parametros:

La funcion `os.path.join()` toma como argumento uno ó mas componentes *(cadenas)* de una ruta, que pueden ser directorios o nombres de archivo.

#### ej:
```python
import os

directorio = "mis_archivos"
archivo = "archivo.txt"

ruta_completa = os.path.join(directorio, archivo)
print(ruta_completa) # out: mis_archivos/archivos.txt
```

### Metodo `os.path.abspath()`

El metodo `abspath()` de `os.path` se utiliza para obtener la ruta absoluta de un archivo o directorio. Una rata obsoluta es aquella que especifica la ubicación exacta de un archivo desde la raíz del sistema de archivo.

#### Parámetros: 

- `path`: Una cadena de taxto que representa la ruta en convertir en absoluta.


### Metodo `os.path.dirname()`

El metodo `dirname()` de `os.path` se utiliza para extrar el nombre del diractorio a partir de una ruta de archivo dada.

#### Parámetros

- `path`: Una cadena de texto que representa la ruta del archivo

#### ej:

```python
    import os

    ruta_cumpleta = "/home/usuario/documentos/mi_archivo.txt"
    directorio = os.path.dirname(ruta_completa)
    print(directorio) # out: /home/usuario/documentos
```

**Tambien se puede usar para crear rutas relativas**

```python
import os

ruta1 = "/home/usuario/proyectos/python/script.py"
ruta2 = "/home/usuario/proyectos/datos/resultados.csv"

directorio_comun = os.path.commonpath([ruta1, ruta2])  # Encuentra el directorio común
ruta_relativa = os.path.relpath(ruta2, directorio_comun)  # Calcula la ruta relativa
print(ruta_relativa)  # Imprime: datos/resultados.csv
```