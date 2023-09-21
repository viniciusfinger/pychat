import socket
import threading
import sys
import os

host = '0.0.0.0'
folder_path = "files"
port = port = int(sys.argv[1]) if len(sys.argv) > 1 else 19000
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
    
    def send_message(self, message):
        self.socket.send((message).encode(utf_8_encoding))

def is_command(message):
    return message[0] == '@'

def process_command(command, client):
    match command.upper():
        case "@LISTDOWNLOADS":
            list_files_to_download(client)

def list_files_to_download(client):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        for index, file in enumerate(files):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                client.send_message(str(index) + ' - ' + file)



def handle_client(client):
    try: 
        client_is_connected = client.socket is not None
        notify_other_clients("[Servidor]: '%s' se conectou ao chat." %str(new_client.username), client)

        while client_is_connected:
            message = client.socket.recv(data_payload_limit).decode(utf_8_encoding)
            
            if message:
                if is_command(message):
                    process_command(message, client)
                else: 
                    message = client.username + ": " + message
                    print(message)
                    notify_other_clients(message, client)

    except socket.error as e:
        print("[Servidor]: Erro no socket: %s" %str(e))
        disconnect_all_clients()
        server_socket.close()
    except Exception as e:
        print("[Servidor]: Erro inesperado: %s" %str(e))
        disconnect_all_clients()
        server_socket.close()
        raise e

def notify_other_clients(message, client_to_not_notify):
    with lock:
        for listener_client in clients_listening: 
            if listener_client != client_to_not_notify:
                listener_client.sendMessage(message)

def disconnect_all_clients():
    for client in clients_listening:
        client.socket.close()

## Adidionar aqui a criação da pasta /files caso nao exista

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

        print("[Servidor]: usuário '%s' conectado." %new_client.username)

        new_client.send_message("[Servidor]: Bem-vindo, %s. Para listar os comandos, digite @AJUDA" %str(new_client.username))

        client_handling_thread = threading.Thread(target=handle_client, args=(new_client,))
        client_handling_thread.start()