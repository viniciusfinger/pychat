
# Pychat 🐍💬

Um chat no terminal usando Python + sockets de rede


## Como usar 🤔

Para usar, usando o seu terminal navegue até o diretório que contém os arquivos `chat_server` e `chat_client`.

Inicie o servidor usando o comando `python3 chat_server.py`. A partir disso, você terá um servidor na porta `12345`.

Para iniciar o cliente, use o comando `python3 chat_client.py`. Automaticamente se conectará ao servidor no localhost.

## To-do
- [x]  Criar estrutura para encapsular clientes
- [x]  Criar estrutura de subscribers para repassar as mensagens para os clientes
- [x]  Ao enviar mensagem, o cliente não pode ficar com a mensagem repetida (talvez um if validando se client != listener_client)
- [x]  Adicionar lock na lista compartilhada entre threads
- [x]  Avisar todos listeners que um cliente novo foi conectado
- [ ]  Encapsular o método send do socket na classe client
- [ ]  Criar estrutura para armazenamento de mensagens no cliente que permita ordenação por hora (talvez encapsular as mensagens.)
- [ ]  Criar uma forma de armazenar arquivos no servidor e transitar isso para o cliente
- [ ]  Criar uma forma do cliente enviar arquivos para o servidor


## Contribuindo ⚒️

Contribuições são sempre bem-vindas!

Para enviar suas alterações, clone o projeto, crie sua branch, faça as devidas alterações e/ou melhorias e então abra um pull request para ser verificado. 
## Referência

 - [Javachat](https://github.com/viniciusfinger/javachat)
 - [Socket - Python docs](https://docs.python.org/3/library/socket.html)

