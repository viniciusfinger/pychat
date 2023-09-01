import socket


host = 'localhost'
port = 12345
encoding = 'utf-8'

data_payload_limit = 2048 

def proccess_client(conn, addr):
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
        print("Error: %s" %str(e))


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = (host, port)
server_socket.bind(server_address)

server_socket.listen(5)
print("Server runing")

while True:
    conn, addr = server_socket.accept()
    
    proccess_client(conn, addr)

server_socket.close()