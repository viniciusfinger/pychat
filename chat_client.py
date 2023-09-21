import socket
import threading
import sys
from datetime import datetime
from os import name, system

if len(sys.argv) < 2:
    print("Usage: python3 chat_client.py SERVER_IP PORT")

host = sys.argv[1]
port = int(sys.argv[2])
utf_8_encoding = 'utf-8'
data_payload_limit = 2048
run_program = True
_message_history = []

class Message(object):
    def __init__(self, content):
        self.content = content
        self.receive_date = datetime.now()

    def print(self):
        print(self.content)

    def print_with_time(self):
        print(self.receive_date.strftime("%H:%M:%S") + " " + self.content)

def append_message(new_message):
    if len(_message_history) >= 15:
        _message_history.pop(0)
    _message_history.append(new_message)

def print_last_messages():
    for message in _message_history:
        message.printWithTime()

def is_command(message):
    return message[0] == '@'

def process_incoming_messages(client_socket): 
    global run_program
    while run_program:
        message_content = client_socket.recv(data_payload_limit).decode(utf_8_encoding)
        message = Message(message_content)
        
        message.print()
        append_message(message)
    
    client_socket.close()
    sys.exit()

def print_help():
    print("--------------------------------")
    print("Comandos possíveis:")
    print("@ORDENAR -> exibe as últimas 15 mensagens")
    print("@SAIR -> encerrar o chat")
    print("@LIMPAR -> limpar o chat")
    print("--------------------------------")

def clear_chat():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def process_command(command):
    global run_program

    match command.upper():
        case "@AJUDA":
            print_help()
        case "@ORDENAR":
            print_last_messages()
        case "@SAIR":
            run_program = False
        case "@LIMPAR":
            clear_chat()
        case _:
            print("Comando inválido. Digite novamente.")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port)
client_socket.connect(server_address)

proccess_incoming_message_thread = threading.Thread(target=process_incoming_messages, args=(client_socket,), daemon=True)
proccess_incoming_message_thread.start()

while run_program:
    try:
        input_content = input()

        if is_command(input_content):
            process_command(input_content)
        else:
            message = Message(input_content)
            append_message(message)
            client_socket.send(message.content.encode(utf_8_encoding))

    except socket.error as e:
        client_socket.close()
        print("Socket error: %s" %str(e))
    except Exception as e:
        client_socket.close()
        print("Unexpected error: %s" %str(e))
        raise e