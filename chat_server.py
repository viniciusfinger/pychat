import socket
import threading

host = 'localhost'
port = 12345
utf_8_encoding = 'utf-8'
data_payload_limit = 2048

class Client(object):
    def __init__(self, socket, address, username):
        self.socket = socket
        self.address = address
        self.username = username

def handle_client(client):
    try: 
        client_connected = client.socket is not None

        while client_connected:
            message = client.socket.recv(data_payload_limit).decode(utf_8_encoding)
            if message:
                print(message)
                client.socket.send(("200 OK message received").encode(utf_8_encoding))
    except socket.error as e:
        print("Socket error: %s" %str(e))
    except Exception as e:
        print("Unexpected error: %s" %str(e))
        raise e


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print("Server started.")

    while True:
        # ver se tem uma forma de mover isso aqui para um builder, evitando todas essas chamadas usando o socket
        # com o objeto desestruturado
        client_socket, client_address = server_socket.accept()
        
        client_socket.send(("[Servidor]: Insira seu nome de usuário: ").encode(utf_8_encoding))
        username = client_socket.recv(data_payload_limit).decode(utf_8_encoding)

        client_socket.send(("[Servidor]: Bem-vindo, %s." %str(username)).encode(utf_8_encoding))
        #até aqui.

        print("User %s connected." %username)

        client = Client(client_socket, client_address, username)

        client_processing_thread = threading.Thread(target=handle_client, args=(client,))
        client_processing_thread.start()