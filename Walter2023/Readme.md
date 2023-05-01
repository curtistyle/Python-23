# FLASK

## ` mysql.connection.cursor() ` en **Flask-mysqldb**

En Flask, `mysql.connection.cursor()` se utiliza para crear un objeto cursor que permite ejecutar consultas en la base de datos MySQL. Este objeto se utiliza para enviar comandos SQL a la base de datos y obtener los resultados.

Para utilizar `mysql.connection.cursor()`, primero debes asegurarte de tener correctamente configurada la conexión a la base de datos MySQL en Flask, es decir, haber establecido las credenciales de acceso y el nombre de la base de datos a la que deseas conectarte.

Una vez que tienes la conexión a la base de datos, puedes crear un objeto cursor utilizando el método `cursor()` de la conexión, de la siguiente manera:

``` python
from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la conexión a la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'usuario'
app.config['MYSQL_PASSWORD'] = 'contraseña'
app.config['MYSQL_DB'] = 'nombre_de_la_base_de_datos'

# Crear una instancia de MySQL y establecer la conexión
mysql = MySQL(app)

# Crear un objeto cursor
cursor = mysql.connection.cursor()
```

Una vez que tienes el objeto cursor, puedes utilizar sus métodos para ejecutar comandos SQL y obtener los resultados, por ejemplo:

``` python
# Ejecutar una consulta SELECT
cursor.execute('SELECT * FROM tabla')

# Obtener los resultados
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)
```

Es importante recordar cerrar el objeto cursor después de utilizarlo, utilizando el método `close()` de la conexión, de la siguiente manera:

```python
# Cerrar el objeto cursor
cursor.close()
```

## execute() en **Flask-mysqldb**

`execute()` es un método de Flask utilizado para ejecutar consultas SQL en una base de datos. Este método se utiliza en conjunto con un **objeto cursor**, que se crea a partir de una conexión a una base de datos, como por ejemplo la conexión a una base de datos MySQL.

El método `execute()` recibe como parámetro una cadena de texto que representa la consulta SQL que se desea ejecutar. Esta cadena de texto puede contener **placeholders**, que se utilizan para pasar valores dinámicamente a la consulta. Por ejemplo, si se desea ejecutar una consulta **SELECT** en una tabla llamada "*usuarios*" que recupere todos los registros cuyo nombre de usuario sea igual a un valor especificado dinámicamente, se puede escribir la consulta de la siguiente manera:

```python
nombre_de_usuario = 'jdoe'
cursor.execute('SELECT * FROM usuarios WHERE nombre_de_usuario = %s', (nombre_de_usuario,))
```

En este ejemplo, `%s` es un **placeholder** que se utiliza para indicar el lugar donde se debe insertar el valor del nombre de usuario en la consulta. El valor del nombre de usuario se pasa como una tupla al método `execute()`, donde el valor se ubica en la primera posición. Es importante notar que el valor se pasa como una tupla, incluso si solo hay un valor a pasar.

Una vez que se ha ejecutado la consulta utilizando el método `execute()`, se pueden recuperar los resultados utilizando otros métodos del objeto cursor, como `fetchall()`, `fetchone()`, etc.

Es importante tener en cuenta que el uso de placeholders en la consulta es importante para prevenir ataques de inyección de SQL, por lo que siempre se deben utilizar para pasar valores dinámicamente a una consulta SQL.

## Query o Consultas en **Flask-mysqldb** 

En Flask, se pueden realizar los siguientes tipos de consultas a una base de datos SQL utilizando diferentes extensiones:

1. Consultas SELECT: se utilizan para recuperar datos de una o varias tablas de la base de datos. Por ejemplo:

```python
from flask_mysqldb import MySQL

mysql = MySQL()

# Consulta SELECT utilizando Flask-MySQL
resultados = mysql.connection.cursor().execute('SELECT * FROM tabla')

# Consulta SELECT utilizando Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tabla(db.Model):
    __tablename__ = 'tabla'
    id = db.Column(db.Integer, primary_key=True)
    columna1 = db.Column(db.String(50))
    columna2 = db.Column(db.String(50))

resultados = Tabla.query.all()
```

2. Consultas INSERT: se utilizan para insertar nuevos registros en una tabla de la base de datos. Por ejemplo:

```python
from flask_mysqldb import MySQL

mysql = MySQL()

# Consulta INSERT utilizando Flask-MySQL
mysql.connection.cursor().execute("INSERT INTO tabla (columna1, columna2) VALUES ('valor1', 'valor2')")

# Consulta INSERT utilizando Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

registro = Tabla(columna1='valor1', columna2='valor2')
db.session.add(registro)
db.session.commit()
```

3. Consultas UPDATE: se utilizan para actualizar registros existentes en una tabla de la base de datos. Por ejemplo:

```python
from flask_mysqldb import MySQL

mysql = MySQL()

# Consulta UPDATE utilizando Flask-MySQL
mysql.connection.cursor().execute("UPDATE tabla SET columna1 = 'nuevo_valor' WHERE id = 1")

# Consulta UPDATE utilizando Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

registro = Tabla.query.filter_by(id=1).first()
registro.columna1 = 'nuevo_valor'
db.session.commit()
```

4. Consultas DELETE: se utilizan para eliminar registros existentes en una tabla de la base de datos. Por ejemplo:

```python
from flask_mysqldb import MySQL

mysql = MySQL()

# Consulta DELETE utilizando Flask-MySQL
mysql.connection.cursor().execute("DELETE FROM tabla WHERE id = 1")

# Consulta DELETE utilizando Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

registro = Tabla.query.filter_by(id=1).first()
db.session.delete(registro)
db.session.commit()
```

Es importante tener en cuenta que el uso de extensiones como Flask-MySQL o Flask-SQLAlchemy puede variar la sintaxis de las consultas SQL dependiendo de la implementación de cada extensión. Además, es importante utilizar placeholders en las consultas para prevenir ataques de inyección de SQL.

## Asterisco * 

El asterisco (*) en `SELECT * FROM tabla WHERE id = %s', (id,)` de Flask significa que se seleccionarán todas las columnas de la tabla "`tabla`". En otras palabras, es una forma abreviada de indicar que se desea seleccionar todos los campos de la tabla.

Es común utilizar esta notación en consultas `SELECT` cuando se desea recuperar todos los campos de una tabla. Sin embargo, también es posible seleccionar campos específicos de una tabla en lugar de utilizar el asterisco. Por ejemplo, si solo se desea seleccionar el campo "`nombre`" de la tabla "`usuarios`", la consulta sería `SELECT nombre FROM usuarios`.

En el caso de la consulta de Flask, el asterisco se utiliza para seleccionar todos los campos de la tabla "`tabla`" donde el valor del campo "`id`" es igual a la variable "`id`" proporcionada en la consulta. La coma seguida de `(id,)` indica que se trata de una tupla con un solo elemento, en este caso la variable "`id`". Esto es necesario porque Flask utiliza parámetros de consulta para evitar la inyección de SQL. El valor de la variable "`id`" se reemplaza en la consulta con el símbolo "`%s`".


## doble asterisco en parametros

En `psycopg2.connect(**db_params), el doble asterisco (**)` es un operador que permite desempaquetar un diccionario en sus elementos clave y valor. En otras palabras, el operador convierte el diccionario `db_params` en una serie de argumentos clave-valor que se pasan a la función `psycopg2.connect()`.

Por ejemplo, si `db_params` es un diccionario que contiene los siguientes elementos:

```python
db_params = {'user': 'usuario', 'password': 'contraseña', 'host': 'localhost', 'port': '5432', 'database': 'basedatos'}
```

El operador de doble asterisco desempaqueta el diccionario en sus elementos clave-valor y los pasa como argumentos a `psycopg2.connect()`, de manera que la llamada sería equivalente a escribir lo siguiente:

```python
psycopg2.connect(user='usuario', password='contraseña', host='localhost', port='5432', database='basedatos')
```

El operador de doble asterisco es especialmente útil cuando se trabaja con funciones que requieren múltiples argumentos, ya que permite pasar los argumentos como un diccionario, lo que puede ser más claro y fácil de leer que escribir los argumentos individualmente. Además, permite agregar o eliminar argumentos sin tener que modificar el código que llama a la función.

## Metodo `request` de Flask

El método `request` de Flask es una variable global que proporciona información sobre la solicitud HTTP actual. Esta variable es un objeto de la clase `Request` de Werkzeug, que es una biblioteca que proporciona herramientas para manejar solicitudes y respuestas HTTP en Python.

El objeto `request` contiene información sobre la solicitud, como la URL, el método HTTP (GET, POST, etc.), los datos de la solicitud (por ejemplo, los parámetros de la URL o los datos del formulario enviado), las cabeceras de la solicitud y más.

A continuación, se describen algunos de los métodos y atributos más útiles del objeto `request`:

> - `request.method`: devuelve el método HTTP de la solicitud, como 'GET', 'POST', 'PUT', 'DELETE', etc.
> - `request.args`: devuelve un diccionario que contiene los parámetros de la URL de la solicitud (si los hay). Por ejemplo, si la URL de la solicitud es `http://localhost:5000/hola?nombre=Juan`, `request.args` contendrá `{'nombre': 'Juan'}`.  
> - `request.form`: devuelve un diccionario que contiene los datos enviados en un formulario HTML mediante el método POST. Por ejemplo, si un formulario contiene un campo llamado `nombre` con el valor `Juan`, `request.form` contendrá `{'nombre': 'Juan'}`.  
> - `request.files`: devuelve un diccionario que contiene los archivos enviados en un formulario HTML mediante el método POST. Cada elemento del diccionario es un objeto `FileStorage`, que proporciona información sobre el archivo (nombre, tipo, tamaño, etc.) y métodos para leer el contenido del archivo.
> - `request.headers`: devuelve un objeto `Headers` que contiene las cabeceras de la solicitud.
> - `request.cookies`: devuelve un diccionario que contiene las cookies enviadas en la solicitud.
> - `request.url`: devuelve la URL de la solicitud completa, incluyendo el protocolo, el nombre de host, el puerto y la ruta.
> - `request.endpoint`: devuelve el nombre de la función de vista que maneja la solicitud actual.

Estos son solo algunos de los métodos y atributos que se pueden utilizar con el objeto `request`. Flask y Werkzeug proporcionan muchas más herramientas para trabajar con solicitudes y respuestas HTTP en Python.

## Metodo `close()` de psycopg2 


El método `close()` de psycopg2 cierra la conexión actual a la base de datos. Esta acción libera todos los recursos utilizados por la conexión, como la memoria y los sockets de red.

Cuando se llama al método `close()`, la conexión se marca como cerrada y no se pueden realizar más operaciones en ella. Si se intenta realizar alguna operación después de cerrar la conexión, se producirá un error.

Es importante cerrar la conexión después de utilizarla para evitar dejar conexiones abiertas innecesariamente. Las conexiones abiertas pueden consumir recursos del servidor y pueden impedir que otras aplicaciones se conecten a la base de datos.

El método `close()` se puede llamar directamente en el objeto `connection` devuelto por la función `connect()`, como en el siguiente ejemplo:

```python
import psycopg2

conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword")
# Hacer alguna operación con la conexión
conn.close()
```

También se puede utilizar la conexión como un contexto de `with`, que cerrará automáticamente la conexión al final del bloque, como en el siguiente ejemplo:

```python
import psycopg2

with psycopg2.connect(database="mydatabase", user="myuser", password="mypassword") as conn:
    # hacer alguna operación con la conexión
    pass
# la conexión se cerrará automáticamente al salir del bloque "with"
```

Es importante tener en cuenta que, aunque el método `close()` cierra la conexión actual, no garantiza que se elimine completamente de la memoria del servidor de la base de datos. Por esta razón, es recomendable cerrar todas las conexiones que no se están utilizando y no dejarlas abiertas innecesariamente.

## Metodo `fetchone()` de psycopg2

El método `fetchone()` de `psycopg2` se utiliza para recuperar la siguiente fila de un resultado de una consulta SQL. Este método se llama en un objeto de cursor que se ha utilizado para ejecutar una consulta.

Después de ejecutar una consulta, el objeto de cursor mantiene un puntero interno que apunta a la primera fila del resultado de la consulta. El método `fetchone()` devuelve la fila a la que apunta el puntero y luego mueve el puntero a la siguiente fila en el resultado.

Por lo tanto, cada vez que se llama al método `fetchone()`, se devuelve la siguiente fila en el resultado de la consulta. Si ya se han devuelto todas las filas del resultado, el método devuelve `None`.

El método `fetchone()` se utiliza comúnmente en combinación con un bucle `while` para recuperar todas las filas de un resultado. Por ejemplo:

```python
cur = conn.cursor()
cur.execute("SELECT * FROM mytable")

row = cur.fetchone()
while row is not None:
    # procesar la fila aquí
    print(row)

    # obtener la siguiente fila
    row = cur.fetchone()

# cerrar el cursor
cur.close()
```

En este ejemplo, se crea un objeto de cursor y se ejecuta una consulta que selecciona todas las filas de la tabla `mytable`. Luego, se llama al método `fetchone()` para obtener la primera fila del resultado, y se utiliza un bucle `while` para procesar cada fila en el resultado hasta que se hayan devuelto todas las filas. Finalmente, se cierra el cursor para liberar los recursos del sistema.

En resumen, el método `fetchone()` de `psycopg2` se utiliza para recuperar la siguiente fila de un resultado de una consulta SQL. Se llama en un objeto de cursor y devuelve la fila a la que apunta el puntero interno del cursor. Este método se utiliza comúnmente en combinación con un bucle `while` para recuperar todas las filas de un resultado.

## Metodo `fetchall()` de psycopg2

El método `fetchall()` de `psycopg2` se utiliza para recuperar todas las filas restantes de un resultado de una consulta SQL. Este método se llama en un objeto de cursor que se ha utilizado para ejecutar una consulta.

Después de ejecutar una consulta, el objeto de cursor mantiene un puntero interno que apunta a la primera fila del resultado de la consulta. El método `fetchall()` devuelve una lista que contiene todas las filas restantes en el resultado de la consulta, comenzando desde la fila actual.

Por lo tanto, si se llama al método `fetchall()` después de haber llamado al método `fetchone()`, la lista devuelta contendrá todas las filas restantes después de la fila devuelta por `fetchone()`. Si nunca se ha llamado al método `fetchone()`, el método `fetchall()` devolverá todas las filas en el resultado de la consulta.

Es importante tener en cuenta que el método `fetchall()` puede consumir una gran cantidad de memoria si el resultado de la consulta es muy grande. Por lo tanto, se recomienda utilizar el método `fetchall()` solo para consultas que devuelven un número limitado de filas.

Aquí hay un ejemplo de cómo se puede usar el método `fetchall()`:

```python
cur = conn.cursor()
cur.execute("SELECT * FROM mytable")

rows = cur.fetchall()
for row in rows:
    # procesar la fila aquí
    print(row)

# cerrar el cursor
cur.close()
```

En este ejemplo, se crea un objeto de cursor y se ejecuta una consulta que selecciona todas las filas de la tabla `mytable`. Luego, se llama al método `fetchall()` para recuperar todas las filas restantes en el resultado de la consulta. Finalmente, se utiliza un bucle `for` para procesar cada fila en la lista devuelta por `fetchall()`, y se cierra el cursor para liberar los recursos del sistema.

En resumen, el método `fetchall()` de `psycopg2` se utiliza para recuperar todas las filas restantes de un resultado de una consulta SQL. Se llama en un objeto de cursor y devuelve una lista que contiene todas las filas restantes en el resultado de la consulta. Es importante tener en cuenta que el método `fetchall()` puede consumir una gran cantidad de memoria si el resultado de la consulta es muy grande.


## Metodo `commit()` de psycopg2

El método `commit()` de `psycopg2` es utilizado para confirmar una transacción en una base de datos PostgreSQL. En otras palabras, una vez que se han realizado todas las operaciones que se desean realizar en una transacción, se debe llamar al método `commit()` para asegurarse de que las modificaciones realizadas en la base de datos sean permanentes.

El método `commit()` es utilizado después de ejecutar una o varias operaciones en una transacción utilizando el cursor de la conexión a la base de datos. Por ejemplo, después de insertar, actualizar o eliminar datos en una tabla, se debe llamar al método `commit()` para que los cambios sean efectivos.

El uso del método `commit()` también es importante en el manejo de errores. Si ocurre un error en una transacción, se puede utilizar el método `rollback()` para deshacer todos los cambios realizados desde la última llamada a `commit()`. De esta manera, se evita que la base de datos quede en un estado inconsistente.

Es importante tener en cuenta que el método `commit()` solo debe ser utilizado cuando se han completado todas las operaciones que se desean realizar en una transacción. Si se llama a `commit()` antes de completar todas las operaciones, se pueden introducir errores en la base de datos.

En resumen, el método `commit()` de `psycopg2` es utilizado para confirmar una transacción en una base de datos PostgreSQL, y debe ser llamado después de que se hayan realizado todas las operaciones que se desean realizar en la transacción.


