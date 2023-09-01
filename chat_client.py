import socket

host = 'localhost'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)

client_socket.connect(server_address)

try:
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

except socket.error as e:
    print("Socket error: %s" %str(e))
