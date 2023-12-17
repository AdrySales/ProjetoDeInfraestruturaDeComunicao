# Importa a biblioteca socket para utilizar as funcionalidades de comunicacao por meio de sockets em Python.
from socket import *

# Tamanho do buffer usado para ler/enviar dados em pedacos.
bufferSize = 1024
# Uma tupla que contem o endereco IP do cliente (localhost, "127.0.0.1") e o numero da porta (20001) em que o servidor esta vinculado para receber dados.
clientAddressPort = ("127.0.0.1", 20001)

# Cria um objeto de socket UDP utilizando a familia de enderecos IPv4 (AF_INET) e o tipo de socket datagrama (SOCK_DGRAM).
# Vincula o socket ao endereco especificado em clientAddressPort.
UDPServerSocket = socket(AF_INET, SOCK_DGRAM)
UDPServerSocket.bind(clientAddressPort)

# Após o vínculo, avisa que o servidor está pronto para receber dados.
print("O servidor UDP esta pronto para receber")

# Recebe os primeiros dados enviados pelo cliente usando o metodo recvfrom()
# imprime uma mensagem e abre um arquivo chamado "recebido.txt" em modo de escrita binaria ("wb") para armazenar os dados recebidos.
data,addr = UDPServerSocket.recvfrom(bufferSize)
print ("Received File:",data.strip())
file = open("recebido.jpeg",'wb')

try:
    while data: # É realizado um loop para receber os dados do arquivo e salvá-los localmente. O loop continua ate que ocorra um timeout
        file.write(data) # Grava os dados recebidos no arquivo "recebido.txt".Cada iteracao do loop escreve um pedaco dos dados no arquivo. 
        UDPServerSocket.settimeout(2) # Define um timeout de 2 segundos para o socket. Isso significa que, se nao houver recebimento de dados dentro de 2 segundos, o socket lancara uma excecao do tipo timeout.
        data,addr = UDPServerSocket.recvfrom(bufferSize) # Recebe dados do cliente usando o metodo recvfrom(). data contem os dados recebidos, e addr contem o endereco do cliente.
except timeout:
    file.close()
    print ("File Downloaded")

# Abre o arquivo "recebido.txt" em modo de leitura binaria ("rb") e le a quantidade inicial de dados definida pelo bufferSize.
file = open("recebido.txt","rb") 
data = file.read(bufferSize)

# Envia os dados lidos do arquivo de volta para o cliente em pacotes usando o metodo sendto() do socket.
# O loop continua ate que todos os dados do arquivo tenham sido enviados
while data:
    if(UDPServerSocket.sendto(data, addr)):
        print ("sending ...")
        data = file.read(bufferSize)

# Encerra o socket e o arquivo 
UDPServerSocket.close()
file.close()







