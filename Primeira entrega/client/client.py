# Importando bibliotecas necessárias
from socket import * 

# serverAddressPort e um objeto que contém o endereco IP e a porta que o servidor tá executando
# bufferSize e o tamanho do buffer são utilizados para o envio de pacotes
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Cria um objeto de socket UDP utilizando a familia de enderecos IPv4 (AF_INET) e o tipo de socket datagrama (SOCK_DGRAM)
UDPClientSocket = socket(AF_INET, SOCK_DGRAM)

# Abre o arquivo "teste.txt" em modo de leitura binaria ("rb") e le a quantidade inicial de dados definida pelo bufferSize
file = open("teste.txt","rb") 
data = file.read(bufferSize)

# Envia os dados lidos do arquivo em pacotes para o servidor usando o metodo sendto() do socket. O loop continua ate que todos os dados do arquivo tenham sido enviados.
while data:
    if(UDPClientSocket.sendto(data, serverAddressPort)):
        print ("sending ...")
        data = file.read(bufferSize)


# Fecha o arquivo apos a conclusao do envio.
file.close()

# Abre um novo arquivo chamado "recebido.txt" em modo de escrita binaria para armazenar os dados recebidos. Em seguida, recebe os primeiros dados do servidor.
file = open("recebido.txt", "wb")
data,addr = UDPClientSocket.recvfrom(bufferSize)
print("Recebendo...")


# Tenta receber os dados do arquivo e salvá-los localmente 
# O loop continua ate que ocorra um timeout (tempo limite) especificado no metodo settimeout(), indicando o fim da transmissao. 
# Ao detectar o timeout, o arquivo é fechado, o socket é fechado, e uma mensagem indicando que o download do arquivo foi concluido e exibida.
try:
    while data:
        file.write(data)
        UDPClientSocket.settimeout(2)
        data,addr = UDPClientSocket.recvfrom(bufferSize)
except timeout:
    file.close()
    UDPClientSocket.close()
    print ("File Downloaded")
