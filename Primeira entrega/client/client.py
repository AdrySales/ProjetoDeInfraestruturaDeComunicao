# Importando bibliotecas necessárias
from socket import * 

# serverAddressPort e um objeto que contém o endereco IP e a porta que o servidor tá executando
# tamanhoDoBuffer e o tamanho do buffer são utilizados para o envio de pacotes
clienteEnderecoPorta = ("127.0.0.1", 20001)
tamanhoDoBuffer = 1024

# Cria um objeto de socket UDP utilizando a familia de enderecos IPv4 (AF_INET) e o tipo de socket datagrama (SOCK_DGRAM)
socketDoCliente = socket(AF_INET, SOCK_DGRAM)

#Abre o arquivo "teste.txt" em modo de leitura binaria ("rb") e le a quantidade inicial de dados definida pelo tamanhoDoBuffer
arquivo = open("gato.jpeg","rb") 
dado = arquivo.read(tamanhoDoBuffer)

# Envia os dados lidos do arquivo em pacotes para o servidor usando o metodo sendto() do socket. O loop continua ate que todos os dados do arquivo tenham sido enviados.
while dado:
    if(socketDoCliente.sendto(dado, clienteEnderecoPorta)):
        dado = arquivo.read(tamanhoDoBuffer)

print("Arquivo enviado!")
# Fecha o arquivo apos a conclusao do envio.
arquivo.close()

# Abre um novo arquivo chamado "recebido.txt" em modo de escrita binaria para armazenar os dados recebidos. Em seguida, recebe os primeiros dados do servidor.
arquivo = open("recebido.jpeg", "wb")
dado,addr = socketDoCliente.recvfrom(tamanhoDoBuffer)



# Tenta receber os dados do arquivo e salvá-los localmente 
# O loop continua ate que ocorra um timeout (tempo limite) especificado no metodo settimeout(), indicando o fim da transmissao. 
# Ao detectar o timeout, o arquivo é fechado, o socket é fechado, e uma mensagem indicando que o download do arquivo foi concluido e exibida.
try:
    while dado:
        arquivo.write(dado)
        socketDoCliente.settimeout(2)
        dado,addr = socketDoCliente.recvfrom(tamanhoDoBuffer)
except timeout:
    arquivo.close()
    socketDoCliente.close()
    print ("Arquivo baixado!")
