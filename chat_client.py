import socket
import threading
import sys

host = 'localhost'
port = 12345
utf_8_encoding = 'utf-8'
data_payload_limit = 2048
run_program = True

def process_incoming_messages(client_socket): 
    global run_program
    while run_program:
        message = client_socket.recv(data_payload_limit).decode(utf_8_encoding)
        print(message)
    
    client_socket.close()
    sys.exit()

def is_command(message):
    return message[0] == '@'

def process_command(command):
    global run_program

    match command.upper():
        case "@ORDENAR":
            print("Ordenando mensagens")
        case "@SAIR":
            run_program = False
        case "@UPLOAD":
            print("Upando arquivo.")
        case "@DOWNLOAD":
            print("Baixando arquivo.")
        case _:
            print("Comando inválido. Digite novamente.")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port)
client_socket.connect(server_address)

proccess_incoming_message_thread = threading.Thread(target=process_incoming_messages, args=(client_socket,), daemon=True)
proccess_incoming_message_thread.start()

while run_program:
    try:
        message = input()

        if is_command(message):
            process_command(message)
        else:
            client_socket.send(message.encode('utf-8'))

    except socket.error as e:
        print("Socket error: %s" %str(e))
    except Exception as e:
        print("Unexpected error: %s" %str(e))
        raise e