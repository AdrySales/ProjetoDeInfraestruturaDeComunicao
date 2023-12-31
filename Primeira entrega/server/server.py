# Importa a biblioteca socket para utilizar as funcionalidades de comunicacao por meio de sockets em Python.
from socket import *

# Tamanho do buffer usado para ler/enviar dados em pedacos.
tamanhoDoBuffer = 1024
# Uma tupla que contem o endereco IP do cliente (localhost, "127.0.0.1") e o numero da porta (20001) em que o servidor esta vinculado para receber dados.
servidorEnderecoPorta = ("127.0.0.1", 20001)

# Cria um objeto de socket UDP utilizando a familia de enderecos IPv4 (AF_INET) e o tipo de socket datagrama (SOCK_DGRAM).
# Vincula o socket ao endereco especificado em clienteEnderecoPorta.
socketDoServidor = socket(AF_INET, SOCK_DGRAM)
socketDoServidor.bind(servidorEnderecoPorta)

# Após o vínculo, avisa que o servidor está pronto para receber dados.
print("*******O servidor esta pronto para receber o arquivo*******")

# Recebe os primeiros dados enviados pelo cliente usando o metodo recvfrom()
# imprime uma mensagem e abre um arquivo chamado "arquivoRecebido.txt" em modo de escrita binaria ("wb") para armazenar os dados recebidos.
dado,addr = socketDoServidor.recvfrom(tamanhoDoBuffer)
print ("Arquivo:",dado.strip())
arquivo = open("arquivoRecebido.jpeg",'wb')

try:
    while dado: # É realizado um loop para receber os dados do arquivo e salvá-los localmente. O loop continua ate que ocorra um timeout
        arquivo.write(dado) # Grava os dados recebidos no arquivo "arquivoRecebido.txt".Cada iteracao do loop escreve um pedaco dos dados no arquivo. 
        socketDoServidor.settimeout(2) # Define um timeout de 2 segundos para o socket. Isso significa que, se nao houver recebimento de dados dentro de 2 segundos, o socket lancara uma excecao do tipo timeout.
        dado,addr = socketDoServidor.recvfrom(tamanhoDoBuffer) # Recebe dados do cliente usando o metodo recvfrom(). dado contem os dados recebidos, e addr contem o endereco do cliente.
except timeout:
    arquivo.close()
    print ("O download terminou!!!")

# Abre o arquivo "arquivoRecebido.txt" em modo de leitura binaria ("rb") e le a quantidade inicial de dados definida pelo bufferSize.
arquivo = open("arquivoRecebido.jpeg","rb") 
dado = arquivo.read(tamanhoDoBuffer)

# Envia os dados lidos do arquivo de volta para o cliente em pacotes usando o metodo sendto() do socket.
# O loop continua ate que todos os dados do arquivo tenham sido enviados
while dado:
    if(socketDoServidor.sendto(dado, addr)):
        dado = arquivo.read(tamanhoDoBuffer)

print("Arquivo baixado!")


# Encerra o socket e o arquivo 
socketDoServidor.close()
arquivo.close()







