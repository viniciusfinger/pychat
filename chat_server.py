import socket
import threading

host = 'localhost'
port = 12345
utf_8_encoding = 'utf-8'
data_payload_limit = 2048

def handle_client(client_socket, client_address):
    try: 
        client_connected = client_socket is not None

        while client_connected:
            message = client_socket.recv(data_payload_limit).decode(utf_8_encoding)
            if message:
                print(message)
                client_socket.send(("200 OK message received").encode(utf_8_encoding))
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
        client_socket, client_address = server_socket.accept()
        client_socket.send(("Insira seu nome de usuário: ").encode(utf_8_encoding))
        username = client_socket.recv(data_payload_limit).decode(utf_8_encoding)
        print("username: " + username)
        client_socket.send(("Bem-vindo %s" %str(username)).encode(utf_8_encoding))

        client_processing_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_processing_thread.start()