import mysql.connector
import mysql
import sqlite3
# db = mysql.connector.connect(host="localhost", user="root", password="admin", database="club")
db_params = dict(
    host = "localhost",
    database = "club",
    port = "3306",
    user = "root",
    password = "admin"
)

connection = sqlite3.connect(**db_params)
cursor = connection.cursor()

def buscar_db(nombre : str, cursor):
    """Retorna `True` si el nombre de la base de datos existe."""
    cursor.execute("SHOW DATABASES")
    res = False
    for db in cursor:
        if db[0] == nombre:
            res = True
    return res

def buscar_tabla(nombre : str, cursor):
    """Retorna `True` si el nombre de la base de datos existe."""
    cursor.execute("SHOW TABLES")
    res = False
    for table in cursor:
        if table[0] == nombre:
            res = True 
    return res

def obtener_cabecera_columnas(tabla : str, cursor):
    columnas = []
    if (buscar_tabla(tabla, cursor)):
        cursor.execute(f"SHOW COLUMNS FROM {tabla}")
        res = cursor.fetchall()
        for columna in res:
            columnas.append(columna[0])
        return columnas
    else:
        return [None]

def insertar_fila(data, tabla : str, cursor):
    lista = [None,None]
    cursor.execute(f"INSERT INTO {tabla} (dorsal, name, age, state) VALUES ('{data['dorsal']}', '{data['name']}', '{data['age']}', '{data['state']}')")
    lista[0] = cursor.fetchone()
    connection.commit()
    lista[1] = cursor.rowcount
    return lista

lista = obtener_cabecera_columnas("boca_juniors", cursor)
print(lista)

item = {"dorsal": 4, "name": "Jorge Figal", "age": 29, "state": True}

print(insertar_fila(item, "boca_juniors", cursor))
# (f"insert into persona (name, last_name, email) values ('{name}', '{last_name}', '{email}') returning id")

