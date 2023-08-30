import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 12345

# Lista para almacenar las conexiones de los clientes
client_connections = []

# Función para manejar las conexiones de los clientes
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            # Enviar el mensaje a todos los clientes
            for connection in client_connections:
                if connection != client_socket:
                    connection.send(message)
        except:
            break
    
    # Eliminar la conexión del cliente de la lista
    client_connections.remove(client_socket)
    client_socket.close()

# Función para recibir mensajes del cliente
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            print(message.decode('utf-8'))
        except:
            break


# Configurar el servidor socket.AF_INET -> protocolo IPv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print('Servidor escuchando en {}:{}'.format(HOST, PORT))

# Esperar conexiones entrantes
while True:
    client_socket, client_address = server_socket.accept()
    print('Conexión establecida desde:', client_address)
    client_connections.append(client_socket)
    
    receive_messages(client_socket)
    # Iniciar un hilo para manejar al cliente
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
