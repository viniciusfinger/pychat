import socket
import threading

host = 'localhost'
port = 12345
encoding = 'utf-8'

data_payload_limit = 2048 

def client_handler(conn, addr):
    try: 
        client_connected = conn is not None

        while client_connected:
            message = conn.recv(data_payload_limit).decode(encoding)
            if message:
                print(message)
                conn.send(("200 OK message received").encode(encoding))
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
        conn, addr = server_socket.accept()
        client_processing_thread = threading.Thread(target=client_handler, args=(conn, addr))
        client_processing_thread.start()