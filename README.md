
# Pychat 🐍💬

Um chat no terminal usando Python + sockets de rede


## Como usar 🤔

Usando o terminal navegue até o diretório que contém os arquivos `chat_server.py` e `chat_client.py`.

Inicie o servidor usando o comando `python3 chat_server.py [porta]`. Caso não insira nenhuma porta, o servidor iniciará na porta `19000`.

Para iniciar o cliente, use o comando `python3 chat_client.py [IP do servidor] [Porta do servidor]`.

## To-do
- [x]  Criar estrutura para encapsular clientes
- [x]  Criar estrutura de subscribers para repassar as mensagens para os clientes
- [x]  Ao enviar mensagem, o cliente não pode ficar com a mensagem repetida (talvez um if validando se client != listener_client)
- [x]  Adicionar lock na lista compartilhada entre threads
- [x]  Avisar todos listeners que um cliente novo foi conectado
- [x]  Encapsular o método send do socket na classe client
- [x]  Criar estrutura para armazenamento de mensagens no cliente que permita ordenação por hora (talvez encapsular as mensagens.)
- [x]  Criar comando @AJUDA no cliente para listar os comandos possíveis.
- [X]  Criar variáveis de entrada para o ip e porta do servidor no client.
- [X]  Criar variável de entrada para porta no servidor
- [ ]  Criar uma forma de armazenar arquivos no servidor e transitar isso para o cliente
- [ ]  Criar uma forma do cliente enviar arquivos para o servidor
- [ ]  Testar rodando em duas máquinas diferentes
 
## Contribuindo ⚒️

Contribuições são sempre bem-vindas!

Para enviar suas alterações, clone o projeto, crie sua branch, faça as devidas alterações e/ou melhorias e então abra um pull request para ser verificado. 
## Referência

 - [Javachat](https://github.com/viniciusfinger/javachat)
 - [Socket - Python docs](https://docs.python.org/3/library/socket.html)

