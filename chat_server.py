import socket
import threading

host = 'localhost'
port = 12345
utf_8_encoding = 'utf-8'
data_payload_limit = 2048
clients_listening = []
lock = threading.Lock()

class Client(object):
    def __init__(self, socket, address, username):
        self.socket = socket
        self.address = address
        self.username = username
    
    def build(client_data_tuple):
        client_socket, client_address = client_data_tuple
    
        client_socket.send(("[Servidor]: Insira seu nome de usuário: ").encode(utf_8_encoding))
        username = client_socket.recv(data_payload_limit).decode(utf_8_encoding)

        return Client(client_socket, client_address, username)

def handle_client(client):
    try: 
        client_is_connected = client.socket is not None
        notify_other_clients("[Servidor]: '%s' se conectou ao chat." %str(new_client.username), client)

        while client_is_connected:
            message = client.socket.recv(data_payload_limit).decode(utf_8_encoding)
            
            if message:
                message = client.username + ": " + message
                print(message)
                notify_other_clients(message, client)

    except socket.error as e:
        print("[Servidor]: Erro no socket: %s" %str(e))
    except Exception as e:
        print("[Servidor]: Erro inesperado: %s" %str(e))
        raise e

def notify_other_clients(message, client_to_not_notify):
    with lock:
        for listener_client in clients_listening: 
            if listener_client != client_to_not_notify:
                listener_client.socket.send((message).encode(utf_8_encoding))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print("[Servidor]: Iniciado com sucesso.")

    while True:
        new_client = Client.build(server_socket.accept())

        with lock:
            clients_listening.append(new_client)

        print("[Servidor] usuário '%s' conectado." %new_client.username)

        new_client.socket.send(("[Servidor]: Bem-vindo, %s." %str(new_client.username)).encode(utf_8_encoding))

        client_handling_thread = threading.Thread(target=handle_client, args=(new_client,))
        client_handling_thread.start()