
# Pychat 🐍💬

Um chat no terminal usando Python + sockets de rede

## Como usar 🤔

Usando o terminal navegue até o diretório que contém os arquivos `chat_server.py` e `chat_client.py`.

Primeiro inicie o servidor usando o comando `python3 chat_server.py [Porta]`. Caso não insira nenhuma porta, o servidor iniciará na porta `19000`.

Para iniciar o cliente, use o comando `python3 chat_client.py [IP do servidor] [Porta]`.

Para ver os possíveis comandos, digite `@AJUDA`.
 
## Arquitetura ⚙️
O chat está arquitetado no modelo client-server, ou seja, no meio de todos os clients temos o servidor fazendo o recebimento e distribuição das mensagens.

No `chat_client.py` temos a thread principal do sistema rodando a leitura do terminal e o envio de mensagens ao servidor enquanto em uma thread separada temos o socket escutando as mensagens que estão chegando de outros clients através do servidor. 

No `chat_server.py` a thread principal é reponsável por escutar novos clients querendo se conectar. Quando um client novo se conecta, uma thread nova se cria. Essa nova thread ficará responsável por ouvir a mensagem que está sendo enviada pelo client e redistribui-la para os outros clients conectados no servidor.

Para redistribuir as mensagens, foi seguido o padrão publisher/subscriber, onde todos os clients mantidos em uma lista chamada `clients_listening` são os subscribers e o servidor é o publisher.

## Contribuindo ⚒️

Contribuições são sempre bem-vindas!

Para enviar suas alterações, clone o projeto, crie sua branch, faça as devidas alterações e/ou melhorias e então abra um pull request para ser verificado. 
## Referência

 - [Javachat](https://github.com/viniciusfinger/javachat)
 - [Socket - Python docs](https://docs.python.org/3/library/socket.html)


