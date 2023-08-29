import socket
import threading

# Configuración del cliente
HOST = '127.0.0.1'
PORT = 12345

# Función para recibir mensajes del servidor
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            print(message.decode('utf-8'))
        except:
            break

# Conectar al servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Iniciar un hilo para recibir mensajes
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Enviar mensajes al servidor
while True:
    message = input()
    client_socket.send(message.encode('utf-8'))
