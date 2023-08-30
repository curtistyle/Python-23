# Excepciones

Las excepciones en Python son eventos que ocurren durante la ejecución de un programa que interrumpen el flujo normal de ejecución debido a errores o condiciones inesperadas. Python proporciona un mecanismo para manejar y responder a estas situaciones excepcionales.

Cuando ocurre una excepción, Python detiene la ejecución normal del programa y busca una sección de código que maneje esa excepción. Si no se encuentra un manejo adecuado para la excepción, el programa se detendrá y mostrará un mensaje de error.

El manejo de excepciones en Python se basa en el uso de bloques `try` y `except`. Aquí está cómo funciona:

```python
try:
    # Código que podría generar una excepción
    resultado = 10 / 0  # Intento dividir por cero
except ZeroDivisionError:
    # Manejo de la excepción específica
    print("Error: División por cero")
```

En este ejemplo, el bloque `try` contiene el código que podría generar una excepción (en este caso, una división por cero). Si se produce la excepción especificada (`ZeroDivisionError` en este caso), el flujo de ejecución se desvía al bloque `except` correspondiente. En este bloque, se proporciona el código para manejar la excepción.

Python también proporciona la posibilidad de manejar excepciones de manera más general, capturando cualquier excepción que ocurra:

```python
try:
    # Código que podría generar una excepción
    resultado = 10 / 0  # Intento dividir por cero
except Exception as e:
    # Manejo de cualquier excepción
    print("Error:", e)
```

En este caso, el bloque `except` captura cualquier excepción que herede de la clase base `Exception`. La excepción capturada se asigna a la variable `e`, que se utiliza para mostrar un mensaje de error.

Además de `try` y `except`, también puedes usar bloques `else` y `finally`:

- `else`: Se ejecuta si no se genera ninguna excepción en el bloque `try`.
- `finally`: Siempre se ejecuta, independientemente de si se genera una excepción o no. Se utiliza para liberar recursos o realizar limpieza, por ejemplo, cerrar archivos o conexiones de bases de datos.

```python
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: División por cero")
else:
    print("Resultado:", resultado)
finally:
    print("Fin del bloque try")
```

En resumen, las excepciones en Python permiten manejar situaciones inesperadas o errores de manera controlada en tu programa, evitando que se detenga abruptamente.

https://es.stackoverflow.com/questions/73855/lanzar-una-excepci%C3%B3n-en-python

*example1*
```python
    @Hora.setter
    def Hora(self, value):
        def horaError():
            raise ValueError("Rango de seteo invalido.")
        try:
            if ((value < 0) or (value > 24)):
                horaError()
            else:
                self.__hora = value
        except ValueError as e:
            print("Error: ",e)
       
```
*example2*
```python

```