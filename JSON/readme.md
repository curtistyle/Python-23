# Ficheros

## `open()`

| Caracter  | Significado |
| ------------- | ------------- |
| `r`  | Abierto para lectura, *por defecto*  |
| `w`  | Abierto para escritura, *truncando primero el fichero* |
| `x`  | Abierto para creacion en exclisiva, *falla si el fichero ya existe* |
| `a`  | Abierto para escritura, *añadiendo al final del fichero si existe* |
| `b`  | modo binario |
| `t`  | modo texto *(por defecto)* |
| `+`  | abierto para actualizar *(lectura y escritura)* |


## Excepciones

| Excepcion | Descripcion |
| --------- | ----------- |
| `FileNotFoundError` | Generado cuando se solicita un archivo o directorio pero no existe |
| `FileExistsError` | Se genera al intentar crear un archivo o directorio que ya existe |


## Paquete `os`

El módulo `os` en Python proporciona una manera de utilizar funcionalidades del sistema operativo, como interactuar con el sistema de archivos, trabajar con variables de entorno, y ejecutar comandos del sistema. Aquí hay algunos de los métodos más comunes que ofrece el módulo `os`:

1. **`os.getcwd()`**: Devuelve el directorio actual de trabajo como una cadena de caracteres.

2. **`os.chdir(path)`**: Cambia el directorio de trabajo actual al especificado por `path`.

3. **`os.listdir(path='.')`**: Devuelve una lista de los archivos y directorios en el directorio dado. Si no se proporciona un directorio, se asume el directorio actual.

4. **`os.mkdir(path)`**: Crea un nuevo directorio en el sistema de archivos.

5. **`os.makedirs(path)`**: Crea un directorio y los directorios intermedios necesarios. Por ejemplo, si `path` es `'a/b/c'` y `a` y `b` no existen, este método creará `a`, `b`, y `c`.

6. **`os.remove(path)`**: Elimina el archivo especificado.

7. **`os.rmdir(path)`**: Elimina el directorio especificado. Nota: el directorio debe estar vacío.

8. **`os.removedirs(path)`**: Elimina el directorio y los directorios intermedios si están vacíos.

9. **`os.rename(src, dst)`**: Cambia el nombre de un archivo o directorio de `src` a `dst`.

10. **`os.path.join(path1, path2, ...) `**: Combina uno o más componentes de la ruta en una sola ruta.

11. **`os.path.exists(path)`**: Devuelve `True` si el archivo o directorio en la ruta especificada existe, de lo contrario devuelve `False`.

12. **`os.path.isfile(path)`**: Devuelve `True` si el camino especificado es un archivo, de lo contrario devuelve `False`.

13. **`os.path.isdir(path)`**: Devuelve `True` si el camino especificado es un directorio, de lo contrario devuelve `False`.

14. **`os.environ`**: Un diccionario que contiene todas las variables de entorno disponibles en el sistema.

15. **`os.system(command)`**: Ejecuta el comando dado por `command` en una subshell (se pasa al shell del sistema operativo para su ejecución).

Estos son solo algunos ejemplos de lo que el módulo `os` puede hacer. Es una herramienta muy útil cuando necesitas interactuar con el sistema de archivos o realizar operaciones relacionadas con el sistema operativo desde Python.

## Estruc 1
"Estructura de datos" en programación se refiere a la forma en que organizas y almacenas datos en la memoria de una computadora para su procesamiento eficiente y acceso. Aquí tienes varias definiciones y perspectivas sobre el concepto de estructuras de datos en programación:

1. **Perspectiva General**:
   - **Estructura de Datos**: Un término que engloba diferentes formas de organizar y almacenar datos en programas informáticos para facilitar su manipulación y uso eficiente.

2. **Perspectiva Conceptual**:
   - **Abstracción de Datos**: Una abstracción que describe cómo se almacenan y organizan los datos, ocultando los detalles de implementación y permitiendo a los programadores interactuar con los datos de manera lógica y eficiente.

3. **Perspectiva Práctica**:
   - **Arreglos (Arrays)**: Una estructura de datos que almacena elementos del mismo tipo en ubicaciones contiguas de memoria.
   - **Listas Enlazadas (Linked Lists)**: Una estructura de datos donde cada elemento contiene un valor y una referencia al siguiente elemento.
   - **Pilas (Stacks)**: Una estructura de datos que sigue el principio de "último en entrar, primero en salir" (LIFO) y se utiliza comúnmente para gestionar llamadas de funciones y seguimiento de ejecución.
   - **Colas (Queues)**: Una estructura de datos que sigue el principio de "primero en entrar, primero en salir" (FIFO) y se utiliza para tareas como la administración de tareas en un sistema operativo.
   - **Árboles (Trees)**: Una estructura de datos jerárquica que se utiliza para organizar datos de manera eficiente, como los árboles binarios de búsqueda o los árboles de expresiones.
   - **Grafos (Graphs)**: Una estructura de datos que representa relaciones entre elementos mediante nodos y arcos, y se usa en aplicaciones como redes y sistemas de recomendación.
   - **Tablas Hash (Hash Tables)**: Una estructura de datos que permite un acceso rápido a los datos mediante una función de dispersión que asigna claves a ubicaciones en la memoria.
   - **Colas de Prioridad (Priority Queues)**: Una estructura de datos que organiza elementos según su prioridad y se usa en algoritmos como Dijkstra o A* para búsqueda de rutas.

4. **Perspectiva de Abstracción**:
   - **Tipos de Datos Abstractos (Abstract Data Types, ADT)**: Estructuras de datos que definen operaciones y propiedades abstractas, independientemente de su implementación, como pilas, colas y listas.

5. **Perspectiva de Rendimiento**:
   - **Complejidad de Tiempo y Espacio**: La eficiencia de una estructura de datos se mide en términos de cuánto tiempo y espacio se requiere para realizar operaciones como inserción, eliminación y búsqueda en la estructura.

6. **Perspectiva de Uso**:
   - **Estructuras de Datos Dinámicas vs. Estáticas**: Algunas estructuras, como los arreglos, tienen un tamaño fijo, mientras que otras, como las listas enlazadas, pueden crecer y disminuir según sea necesario.

Estas definiciones y perspectivas ilustran la diversidad y la importancia de las estructuras de datos en la programación y cómo son fundamentales para resolver problemas y optimizar el rendimiento en aplicaciones de software.

## Estruc 2

La "estructura de datos" en programación se refiere a la forma en que los datos están organizados y almacenados en la memoria de una computadora para que puedan ser utilizados de manera efectiva y eficiente. Aquí te presento algunas definiciones de estructuras de datos:

1. **Colección de Datos**: Una estructura de datos es una forma de organizar y almacenar datos para que puedan ser utilizados de manera efectiva.

2. **Contenedor de Datos**: Es una manera de organizar y almacenar datos en la memoria de la computadora para que puedan ser utilizados de manera eficiente.

3. **Manera de Organizar Datos**: Se refiere al diseño y organización de los elementos de datos en la memoria de una computadora o en un archivo para que se puedan utilizar de manera efectiva.

4. **Esquema de Almacenamiento y Operaciones**: Una estructura de datos proporciona un esquema para organizar y almacenar datos, así como operaciones definidas que se pueden realizar en esos datos.

5. **Abstracción para Representar Datos**: Proporciona una abstracción que permite representar los datos de manera organizada y facilita la realización de operaciones sobre esos datos.

6. **Forma de Organizar Datos en una Computadora**: Es la forma en que los datos se organizan en la memoria de una computadora para facilitar el acceso y manipulación.

7. **Modelo de Datos**: Es un modelo conceptual que describe cómo se organizan y manipulan los datos. Puede ser implementado utilizando varias estructuras subyacentes.

8. **Conjunto de Métodos y Estructuras para Operar Datos**: Incluye tanto las estructuras de datos como los métodos (funciones o procedimientos) que operan sobre esos datos.

En resumen, una estructura de datos en programación proporciona una forma de organizar y almacenar datos para que puedan ser utilizados y manipulados de manera efectiva y eficiente en un programa de computadora. Pueden variar en complejidad y se utilizan para diferentes propósitos dependiendo de las necesidades del programa.

# Estructuras de datos en python

Python ofrece varias estructuras de datos incorporadas que son fundamentales para la programación. Aquí están algunas de las estructuras de datos más comunes y sus diferencias:

1. **Listas (`list`)**:
   - Colección ordenada y mutable de elementos.
   - Los elementos pueden ser de cualquier tipo, incluso otra lista.
   - Se pueden acceder mediante un índice.
   - Sintaxis de creación: `mi_lista = [1, 2, 3, 'texto']`.

2. **Tuplas (`tuple`)**:
   - Colección ordenada e inmutable de elementos.
   - Los elementos pueden ser de cualquier tipo, incluso otra tupla.
   - Se pueden acceder mediante un índice.
   - Sintaxis de creación: `mi_tupla = (1, 2, 3, 'texto')`.

3. **Conjuntos (`set`)**:
   - Colección no ordenada de elementos únicos e inmutables.
   - No permite duplicados.
   - No se pueden acceder mediante un índice.
   - Sintaxis de creación: `mi_set = {1, 2, 3, 'texto'}`.

4. **Diccionarios (`dict`)**:
   - Colección no ordenada de pares clave-valor.
   - Las claves deben ser únicas y pueden ser de cualquier tipo inmutable (como cadenas o números).
   - Los valores pueden ser de cualquier tipo.
   - Sintaxis de creación: `mi_dict = {'clave1': 'valor1', 'clave2': 'valor2'}`.

5. **Cadenas (`str`)**:
   - Secuencia inmutable de caracteres Unicode.
   - Pueden ser accedidas por índice, pero son inmutables, lo que significa que no se pueden modificar.
   - Sintaxis de creación: `mi_cadena = "Hola, mundo!"`.

6. **Listas Anidadas**:
   - Listas que contienen otras listas como elementos.
   - Permiten la creación de estructuras de datos más complejas.
   - Sintaxis de creación: `mi_lista_anidada = [[1, 2], [3, 4]]`.

7. **Cadenas de Bytes (`bytes`)**:
   - Similar a las cadenas, pero representan secuencias de bytes en lugar de caracteres Unicode.
   - Son inmutables.
   - Sintaxis de creación: `mis_bytes = b'Hola'`.

8. **Arreglos (`array`)**:
   - Colección de elementos del mismo tipo, similar a una lista, pero más eficiente para ciertas operaciones.
   - Requiere importar el módulo `array`.
   - Sintaxis de creación: `import array; mi_arreglo = array.array('i', [1, 2, 3])`.

Estas son algunas de las estructuras de datos fundamentales en Python. Cada una tiene sus propias características y se elige según los requisitos específicos del problema que estés resolviendo. Por ejemplo, las listas son versátiles y utilizadas ampliamente, mientras que los conjuntos son ideales para operaciones de conjunto, y los diccionarios son eficientes para mapeos clave-valor.