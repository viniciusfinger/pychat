import socket

host = 'localhost'
port = 12345

data_payload_limit = 2048 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = (host, port)
server_socket.bind(server_address)

server_socket.listen(5)
print("Server runing")  

while True:
    client, address = server_socket.accept()
    data = client.recv(data_payload_limit)


    if data:
        client.send(data)
        print(data)
        