# Socket
## `socket.socket()`

El método `socket.socket()` del módulo `socket` en Python se utiliza para crear un objeto de socket que permite la comunicación a través de la red. Los sockets son puntos finales para enviar y recibir datos a través de una red, ya sea en la misma máquina o entre máquinas diferentes en una red.

La sintaxis básica para crear un objeto de socket es la siguiente:

```python
socket_object = socket.socket(family, type, proto)
```

Donde:
- `family` es la familia de direcciones del socket. Puede ser `socket.AF_INET` para IPv4 o `socket.AF_INET6` para IPv6.
- `type` es el tipo de socket. Puede ser `socket.SOCK_STREAM` para sockets de flujo (TCP) o `socket.SOCK_DGRAM` para sockets de datagrama (UDP).
- `proto` es el protocolo. Generalmente se establece en 0 para que el sistema elija automáticamente el protocolo adecuado para el tipo de socket.

Aquí hay un ejemplo de cómo usar `socket.socket()` para crear un objeto de socket TCP:

```python
import socket

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

En este ejemplo, se crea un objeto de socket TCP utilizando la familia de direcciones IPv4 (`AF_INET`) y el tipo de socket de flujo (`SOCK_STREAM`).

Luego, puedes usar métodos como `bind()`, `listen()`, `accept()` (para el servidor) y `connect()` (para el cliente) para configurar y establecer la conexión del socket.

Es importante recordar que una vez que hayas terminado de usar el socket, debes cerrarlo utilizando el método `close()` para liberar los recursos correctamente.

En resumen, `socket.socket()` se utiliza para crear un objeto de socket que se puede utilizar para establecer conexiones de red y enviar y recibir datos a través de la red.

## Tipos de protocolos

En redes de computadoras, existen varios tipos de sockets que se utilizan para establecer comunicaciones entre diferentes dispositivos a través de una red. Los tipos de sockets más comunes son:

1. **Socket de Flujo (TCP - Transmission Control Protocol)**:
   - Se establece una conexión de extremo a extremo antes de la transferencia de datos.
   - Proporciona comunicación confiable y ordenada, adecuada para transferir datos que deben entregarse en el mismo orden en que se enviaron.
   - Garantiza la entrega de datos y maneja la detección y corrección de errores.
   - Utilizado para aplicaciones que requieren transferencia de datos precisa, como navegadores web, correo electrónico y transferencia de archivos.

2. **Socket de Datagrama (UDP - User Datagram Protocol)**:
   - No se establece una conexión antes de la transferencia de datos.
   - Proporciona comunicación no confiable y sin garantía de entrega de datos. Los datos pueden perderse o llegar en un orden diferente.
   - Es más rápido y eficiente que TCP debido a su naturaleza sin conexión.
   - Utilizado para aplicaciones donde la velocidad es crucial y una pérdida ocasional de datos no es crítica, como videojuegos en línea, streaming y transmisiones en vivo.

3. **Socket Crudo (Raw Socket)**:
   - Proporciona acceso de bajo nivel a los paquetes de red, incluidos los encabezados.
   - Se utiliza para implementar protocolos de red personalizados y herramientas de diagnóstico de red.
   - Requiere privilegios de administrador debido a su acceso de bajo nivel.

4. **Socket Unix**:
   - Utilizado en sistemas Unix y similares para la comunicación entre procesos en la misma máquina.
   - Se basa en archivos especiales en el sistema de archivos Unix.

5. **Socket de Secuencia de Paquetes SCTP (Stream Control Transmission Protocol)**:
   - Similar a TCP, pero diseñado para ofrecer características de confiabilidad y entrega en orden en redes más complejas.
   - Adecuado para aplicaciones que requieren transferencia de datos confiable en entornos de red más adversos, como VoIP y telecomunicaciones.

Estos son algunos de los tipos de sockets más comunes utilizados en redes de computadoras. La elección del tipo de socket depende de los requisitos de la aplicación y las características de la red en la que se está trabajando. Cada tipo de socket tiene sus propias ventajas y desventajas en términos de confiabilidad, velocidad y complejidad.

## `Socket.bind()`

El método `socket.bind()` del módulo `socket` en Python se utiliza para enlazar un socket a una dirección y puerto específicos en la máquina local. Esto significa que el socket estará disponible para recibir conexiones entrantes en la dirección y puerto especificados.

La sintaxis básica del método `bind()` es la siguiente:

```python
socket.bind((host, port))
```

Donde:
- `host` es la dirección IP o el nombre de host de la máquina local en la que deseas enlazar el socket. Puede ser una cadena vacía (`''`) para enlazarlo a todas las interfaces de red disponibles.
- `port` es el número de puerto en el que deseas enlazar el socket.

Aquí hay un ejemplo de cómo usar `socket.bind()` para enlazar un socket a una dirección y puerto específicos:

```python
import socket

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 12345       # Puerto para la comunicación

# Crear un socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket al host y puerto
server_socket.bind((HOST, PORT))
```

En este ejemplo, se crea un objeto de socket TCP utilizando la dirección IP `127.0.0.1` (que representa la máquina local) y el puerto `12345`. Luego, el método `bind()` se utiliza para enlazar el socket a esa dirección y puerto.

Es importante tener en cuenta que después de enlazar un socket, puedes usar el método `socket.listen()` para comenzar a escuchar conexiones entrantes en ese socket. Sin embargo, asegúrate de que el puerto que estás utilizando no esté en uso por otros programas en tu sistema.

## `Socket.listen()`

El método `socket.listen()` del módulo `socket` en Python se utiliza para poner un socket en un estado de escucha, lo que significa que el socket estará listo para aceptar conexiones entrantes de clientes.

La sintaxis básica del método `listen()` es la siguiente:

```python
socket.listen(backlog)
```

Donde:
- `backlog` es un número que representa la cantidad máxima de conexiones pendientes que el socket puede mantener en la cola de espera antes de rechazar nuevas conexiones. Este valor generalmente se ajusta según la capacidad del servidor y la carga esperada.

Una vez que has enlazado un socket utilizando `socket.bind()` y luego llamado a `socket.listen()`, el socket está configurado para escuchar conexiones entrantes en la dirección y puerto especificados. Cuando una conexión entrante se detecta, el socket se convierte en un socket de conexión dedicado a esa conexión específica, y el servidor puede usar el método `socket.accept()` para aceptar la conexión entrante y crear un nuevo socket de comunicación para manejarla.

Aquí hay un ejemplo de cómo usar `socket.listen()` en un servidor:

```python
import socket

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 12345       # Puerto para la comunicación

# Crear un socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket al host y puerto
server_socket.bind((HOST, PORT))

# Poner el socket en estado de escucha
server_socket.listen(5)  # Máximo 5 conexiones en espera
```

En este ejemplo, después de enlazar el socket al host y puerto, se llama a `listen(5)` para poner el socket en estado de escucha, con un límite máximo de 5 conexiones en espera. Luego, el servidor está listo para aceptar conexiones entrantes utilizando `socket.accept()`.

## `Socket.accept()`

El método `socket.accept()` del módulo `socket` en Python se utiliza para aceptar una conexión entrante en un socket que está en estado de escucha. Cuando un cliente intenta conectarse al servidor, el método `accept()` aceptará la conexión y creará un nuevo socket dedicado a esa conexión específica.

La sintaxis básica del método `accept()` es la siguiente:

```python
client_socket, client_address = server_socket.accept()
```

Donde:
- `server_socket` es el socket en estado de escucha creado previamente con `socket.socket()` y configurado con `socket.bind()` y `socket.listen()`.
- `client_socket` es el nuevo socket que representa la conexión entrante.
- `client_address` es una tupla que contiene la dirección IP y el puerto del cliente que está realizando la conexión.

Después de llamar a `accept()`, el servidor puede utilizar `client_socket` para comunicarse con el cliente conectado. Es importante tener en cuenta que cada vez que se acepta una conexión entrante, se crea un nuevo socket dedicado para esa conexión específica. Esto permite al servidor manejar múltiples conexiones de forma concurrente utilizando subprocesos o multiprocesos.

Aquí hay un ejemplo de cómo usar `socket.accept()` en un servidor:

```python
import socket

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 12345       # Puerto para la comunicación

# Crear un socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket al host y puerto
server_socket.bind((HOST, PORT))

# Poner el socket en estado de escucha
server_socket.listen(5)  # Máximo 5 conexiones en espera

while True:
    # Aceptar una conexión entrante
    client_socket, client_address = server_socket.accept()
    print('Conexión establecida desde:', client_address)
    
    # Aquí puedes realizar operaciones de comunicación con el cliente utilizando client_socket
    # ...
    
    # Cerrar el socket de cliente
    client_socket.close()
```

En este ejemplo, el bucle `while True` permite al servidor aceptar conexiones entrantes de forma continua. Cada vez que se acepta una conexión, se muestra la dirección del cliente y luego se cierra el socket de cliente después de completar las operaciones de comunicación.

## `Socket.recv()`

El método `socket.recv()` del módulo `socket` en Python se utiliza para recibir datos desde un socket. Permite que un programa reciba datos enviados por otro programa a través de la red.

La sintaxis básica del método `recv()` es la siguiente:

```python
data = socket.recv(buffer_size)
```

Donde:
- `socket` es el socket desde el cual deseas recibir datos.
- `buffer_size` es la cantidad máxima de bytes que deseas recibir en una llamada a `recv()`.
- `data` es el contenido recibido, que generalmente se almacena en una variable.

El método `recv()` bloqueará la ejecución del programa hasta que se reciban los datos especificados o hasta que la conexión se cierre.

Aquí tienes un ejemplo de cómo usar `socket.recv()` para recibir datos en un servidor que acepta conexiones:

```python
import socket

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 12345       # Puerto para la comunicación

# Crear un socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket al host y puerto
server_socket.bind((HOST, PORT))

# Poner el socket en estado de escucha
server_socket.listen(5)

while True:
    # Aceptar una conexión entrante
    client_socket, client_address = server_socket.accept()
    print('Conexión establecida desde:', client_address)
    
    # Recibir datos del cliente
    data = client_socket.recv(1024)  # Recibir hasta 1024 bytes
    
    # Decodificar y mostrar los datos recibidos
    print('Datos recibidos:', data.decode('utf-8'))
    
    # Cerrar el socket de cliente
    client_socket.close()
```

En este ejemplo, después de aceptar una conexión entrante, el servidor utiliza `recv()` para recibir datos del cliente. El método `decode()` se usa para convertir los datos recibidos en una cadena legible en UTF-8. Ten en cuenta que `recv()` devuelve los datos en forma de bytes, por lo que es importante decodificarlos para obtener la representación de cadena adecuada.

## `Socket.send()`

El método `socket.send()` del módulo `socket` en Python se utiliza para enviar datos a través de un socket. Permite que un programa envíe datos a otro programa a través de la red.

La sintaxis básica del método `send()` es la siguiente:

```python
bytes_sent = socket.send(data)
```

Donde:
- `socket` es el socket a través del cual deseas enviar datos.
- `data` es el contenido que deseas enviar, generalmente en forma de bytes.
- `bytes_sent` es el número de bytes que se enviaron correctamente.

Este método devuelve el número de bytes enviados exitosamente. Puede ser menor que el tamaño de los datos enviados en situaciones donde los datos no se puedan enviar de una vez debido a limitaciones en el tamaño del búfer de envío o problemas de red.

Aquí tienes un ejemplo de cómo usar `socket.send()` para enviar datos desde un cliente a un servidor:

```python
import socket

# Configuración del cliente
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 12345       # Puerto para la comunicación

# Crear un socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((HOST, PORT))

# Datos para enviar
data = "Hola, servidor!"

# Enviar datos al servidor
bytes_sent = client_socket.send(data.encode('utf-8'))

print('Bytes enviados:', bytes_sent)

# Cerrar el socket del cliente
client_socket.close()
```

En este ejemplo, el cliente crea un socket y se conecta al servidor. Luego, utiliza `send()` para enviar los datos codificados en bytes al servidor. Recuerda que los datos deben ser codificados antes de ser enviados utilizando `encode()`, ya que `send()` espera datos en forma de bytes.

Una vez que se envían los datos, el método devuelve la cantidad de bytes enviados correctamente, que puede ser menor que el tamaño total de los datos si ocurre una fragmentación debido al tamaño del búfer de envío o problemas de red.

## Todos los metodos `socket`

El módulo `socket` en Python proporciona funciones y clases para trabajar con conexiones de red, lo que permite la comunicación entre programas en diferentes máquinas a través de la red. Aquí tienes algunos de los métodos y funciones más utilizados del módulo `socket` junto con sus descripciones:

1. **`socket.socket(family, type, proto=0)`**:
   - Constructor de la clase `socket`.
   - Crea un objeto de socket que se utiliza para la comunicación de red.
   - `family` especifica la familia de direcciones, como `socket.AF_INET` para IPv4.
   - `type` especifica el tipo de socket, como `socket.SOCK_STREAM` para sockets TCP.

2. **`socket.bind(address)`**:
   - Enlaza un socket a una dirección y un puerto específicos.
   - `address` es una tupla que contiene la dirección IP y el puerto.

3. **`socket.listen(backlog)`**:
   - Pone un socket en estado de escucha para aceptar conexiones entrantes.
   - `backlog` es el número máximo de conexiones en espera.

4. **`socket.accept()`**:
   - Acepta una conexión entrante.
   - Devuelve un nuevo socket para la comunicación con el cliente y la dirección del cliente.

5. **`socket.connect(address)`**:
   - Establece una conexión saliente a una dirección y un puerto remotos.
   - `address` es una tupla que contiene la dirección IP y el puerto.

6. **`socket.send(data)`**:
   - Envía datos a través del socket.
   - `data` es el contenido que se va a enviar.

7. **`socket.recv(buffer_size)`**:
   - Recibe datos del socket.
   - `buffer_size` es la cantidad máxima de bytes para recibir.

8. **`socket.close()`**:
   - Cierra el socket y libera los recursos asociados.

9. **`socket.gethostname()`**:
   - Devuelve el nombre del host local.

10. **`socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)`**:
    - Resuelve una dirección y un puerto en información de dirección.
    - Útil para obtener detalles sobre cómo conectarse a una dirección.

11. **`socket.getsockopt(level, optname, buflen=None)`**:
    - Obtiene el valor de una opción de socket específica.

12. **`socket.setsockopt(level, optname, value)`****:
    - Establece el valor de una opción de socket específica.

13. **`socket.create_connection(address, timeout=None, source_address=None)`**:
    - Crea una conexión de socket saliente y devuelve un objeto de socket conectado.

14. **`socket.gethostbyaddr(ip_address)`** y **`socket.gethostbyname(hostname)`**:
    - Resuelven direcciones IP en nombres de host y viceversa.

Estos son solo algunos de los métodos y funciones clave del módulo `socket` en Python. El módulo `socket` proporciona muchas más funciones y opciones para trabajar con conexiones de red y realizar comunicaciones en programas distribuidos a través de la red.

# threading

El módulo `threading` en Python proporciona una forma de crear y administrar hilos (threads) para realizar múltiples tareas concurrentemente dentro de un programa. Los hilos son subprocesos ligeros que comparten el mismo espacio de direcciones de memoria, lo que permite que múltiples partes del programa se ejecuten de manera concurrente, lo que puede mejorar la eficiencia y la capacidad de respuesta en ciertos casos.

El módulo `threading` facilita la creación y el control de hilos en Python. Algunas de las funcionalidades clave que proporciona son:

1. **Creación de Hilos**: Puedes crear hilos utilizando la clase `Thread` del módulo. Cada instancia de `Thread` representa un hilo independiente en tu programa.

2. **Ejecución Concurrente**: Los hilos permiten que diferentes partes de tu programa se ejecuten en paralelo. Esto es útil para realizar tareas simultáneas, como procesamiento en segundo plano mientras se mantiene la capacidad de respuesta de la interfaz de usuario.

3. **Sincronización**: El módulo proporciona mecanismos para sincronizar hilos, como semáforos, bloqueos y condiciones, para evitar problemas de concurrencia, como la condición de carrera.

4. **Planificación de Hilos**: Los hilos son planificados por el sistema operativo o el intérprete de Python. Puedes usar funciones como `threading.enumerate()` para obtener una lista de todos los hilos en ejecución.

5. **Control de Hilos**: Puedes iniciar y detener hilos, así como esperar a que un hilo termine su ejecución utilizando métodos como `start()`, `join()`, `run()`, entre otros.

6. **Comunicación entre Hilos**: Puedes compartir datos entre hilos utilizando estructuras de datos seguras como `Queue`.

Aquí hay un ejemplo simple de cómo se utiliza el módulo `threading` para ejecutar dos hilos que imprimen mensajes:

```python
import threading

def print_hello():
    for _ in range(5):
        print("Hello")

def print_world():
    for _ in range(5):
        print("World")

# Crear hilos
thread1 = threading.Thread(target=print_hello)
thread2 = threading.Thread(target=print_world)

# Iniciar los hilos
thread1.start()
thread2.start()

# Esperar a que ambos hilos terminen
thread1.join()
thread2.join()

print("Fin del programa")
```

Este es solo un ejemplo básico de cómo el módulo `threading` puede utilizarse para lograr la concurrencia en un programa. Sin embargo, es importante tener en cuenta que trabajar con hilos introduce desafíos adicionales relacionados con la concurrencia y la sincronización, como condiciones de carrera y bloqueos.

## `threading.Thread()`

El método `threading.Thread()` del módulo `threading` en Python se utiliza para crear una instancia de la clase `Thread`, que representa un hilo (thread) en un programa. Esta instancia se utiliza para controlar y administrar ese hilo específico.

La sintaxis básica para crear un objeto `Thread` es la siguiente:

```python
thread = threading.Thread(target=funcion, args=args)
```

Donde:
- `target` es la función que se ejecutará en el hilo.
- `args` es una tupla de argumentos que se pasará a la función `target`.

Una vez que hayas creado un objeto `Thread`, puedes utilizar sus métodos para controlar la ejecución del hilo. Algunos de los métodos más comunes son:

- `start()`: Inicia la ejecución del hilo. Invoca la función `target` con los argumentos especificados en `args`.
- `join()`: Espera a que el hilo termine su ejecución. Si se llama a `join()` en un hilo desde otro hilo, el segundo hilo esperará hasta que el primero haya terminado antes de continuar.
- `is_alive()`: Verifica si el hilo todavía está en ejecución.
- `getName()` y `setName(name)`: Obtienen o establecen el nombre del hilo.

Aquí tienes un ejemplo de cómo usar `threading.Thread()` para crear y controlar un hilo:

```python
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in 'abcde':
        print(letter)

# Crear instancias de Thread
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Iniciar los hilos
thread1.start()
thread2.start()

# Esperar a que ambos hilos terminen
thread1.join()
thread2.join()

print("Fin del programa")
```

En este ejemplo, se crean dos objetos `Thread` que ejecutan las funciones `print_numbers` y `print_letters`. Luego, se inician los hilos llamando a `start()` y se espera a que ambos hilos terminen utilizando `join()` antes de que se imprima el mensaje final.

Es importante tener en cuenta que el uso de hilos conlleva consideraciones de concurrencia y sincronización. Asegúrate de manejar correctamente los problemas de acceso simultáneo a recursos compartidos para evitar condiciones de carrera u otros problemas de concurrencia.

## `threading.start()`

El método `start()` del módulo `threading` en Python se utiliza para iniciar la ejecución de un hilo creado utilizando la clase `Thread`. Llamar a este método hace que el hilo ejecute la función especificada como su objetivo (`target`) de manera independiente y concurrente.

Después de llamar a `start()`, el hilo se activa y comienza a ejecutar la función `target` con los argumentos proporcionados.

La sintaxis básica para iniciar un hilo es la siguiente:

```python
thread.start()
```

Donde `thread` es una instancia de la clase `Thread` que se ha creado previamente utilizando `threading.Thread()`.

Aquí tienes un ejemplo de cómo usar `start()` para iniciar un hilo:

```python
import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)  # Simula una pequeña espera

# Crear un objeto Thread
thread = threading.Thread(target=print_numbers)

# Iniciar el hilo
thread.start()

print("Hilo iniciado")

# Esperar a que el hilo termine
thread.join()

print("Hilo terminado")
```

En este ejemplo, se crea un objeto `Thread` que ejecutará la función `print_numbers()`. Luego, se llama a `start()` para iniciar el hilo. El hilo imprimirá los números del 1 al 5, pero debido a la pausa de 1 segundo en cada iteración, verás que los mensajes se intercalan con el mensaje "Hilo iniciado". Finalmente, se espera a que el hilo termine su ejecución utilizando `join()` antes de imprimir el mensaje "Hilo terminado".

Es importante recordar que solo se debe llamar a `start()` una vez en un objeto `Thread`. Si intentas iniciar un hilo que ya ha comenzado o ha terminado, se producirá un error.

## Todos los metodos `threading`

El módulo `threading` en Python proporciona varias clases y funciones para trabajar con hilos (threads) y concurrencia. Aquí están algunos de los métodos y funciones más utilizados del módulo `threading` junto con sus descripciones:

1. **`Thread(target, args=())`**:
   - Constructor de la clase `Thread`.
   - Crea una instancia de un hilo.
   - `target` es la función que el hilo ejecutará.
   - `args` es una tupla de argumentos que se pasan a la función `target`.

2. **`Thread.start()`**:
   - Inicia la ejecución del hilo.
   - El hilo ejecutará la función `target` con los argumentos especificados en `args`.

3. **`Thread.join(timeout=None)`**:
   - Espera a que el hilo termine su ejecución.
   - Si se proporciona un valor `timeout`, el método esperará hasta ese tiempo antes de continuar.

4. **`Thread.is_alive()`**:
   - Verifica si el hilo todavía está en ejecución.

5. **`Thread.getName()`** y **`Thread.setName(name)`**:
   - Obtienen o establecen el nombre del hilo.

6. **`threading.current_thread()`**:
   - Devuelve la instancia del hilo actual.

7. **`threading.enumerate()`**:
   - Devuelve una lista de todos los hilos activos en el programa.

8. **`threading.active_count()`**:
   - Devuelve el número de hilos activos en el programa.

9. **`threading.Lock()`** y **`threading.RLock()`**:
   - Proporcionan bloqueos (locks) para sincronización.
   - `Lock` permite que solo un hilo acceda a un recurso compartido a la vez.
   - `RLock` permite a un hilo adquirir el mismo bloqueo varias veces.

10. **`threading.Event()`**:
    - Proporciona una forma de comunicación entre hilos basada en señales.
    - Puede estar en estado "apagado" o "encendido". Los hilos pueden esperar a que el evento se encienda antes de continuar.

11. **`threading.Condition()`**:
    - Proporciona una forma de sincronizar hilos basada en una condición.
    - Permite a los hilos esperar hasta que se cumpla cierta condición antes de continuar.

12. **`threading.Semaphore(value=1)`**:
    - Proporciona un contador para controlar el acceso simultáneo a recursos compartidos.
    - El valor inicial especifica cuántos hilos pueden adquirir el semáforo simultáneamente.

13. **`threading.Timer(interval, function, args=())`**:
    - Crea un hilo que ejecuta la función después de un intervalo dado.

Estos son solo algunos de los métodos y funciones clave del módulo `threading` en Python. Cada uno de ellos tiene un propósito específico en la gestión y control de hilos, permitiendo una programación concurrente más eficiente y segura.

