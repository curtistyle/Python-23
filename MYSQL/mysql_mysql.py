import mysql.connector
from mysql.connector import Error


def crear_conexion(host, user, password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        print("Conexion a la base de datos MYSQL exitosa!")
    except Error as e:
        print(f"Ocurrio el error: {e}")

    return connection

def crear_db(connection, db_name : str):
    """`connection` es el objeto de conexión al servidor de base datos con el que desea interactuar. `db_name` es el nombre de la base de datos."""
    cursor = connection.cursor()
    try:
        
        cursor.execute(f"CREATE DATABASE {db_name}")
        print("Base de datos creada existosamente!")
    except Error as e:
        print(f"Ocurrio el error: {e}")


def crear_conexion_db(host, user, password, database):
    connection = None
    try: 
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Conexion a la base de datos MYSQL exitosa!")
    except Error as e:
        print(f"Ocurrio un error: {e}")
    
    return connection

def buscar_tabla(nombre : str, cursor):
    """Retorna `True` si el nombre de la base de datos existe."""
    cursor.execute("SHOW TABLES")
    res = False
    for table in cursor:
        if table[0] == nombre:
            res = True 
    return res

conn = crear_conexion_db("localhost", "root", "admin", "club")

conn.close()