import socket
import threading

host = 'localhost'
port = 12345
utf_8_encoding = 'utf-8'
data_payload_limit = 2048

def process_incoming_messages(client_socket): 
    while True:
        message = client_socket.recv(data_payload_limit).decode(utf_8_encoding)
        print(message)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port)
client_socket.connect(server_address)

proccess_incoming_message_thread = threading.Thread(target=process_incoming_messages, args=(client_socket,))
proccess_incoming_message_thread.start()

while True:
    try:
        message = input()
        client_socket.send(message.encode('utf-8'))

    except socket.error as e:
        print("Socket error: %s" %str(e))

    except Exception as e:
        print("Unexpected error: %s" %str(e))
        raise e
