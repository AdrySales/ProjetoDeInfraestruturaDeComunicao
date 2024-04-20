from socket import *

class RDT:
    def __init__(self, servidor=False):
        self.endereco = ("localhost", 20001)
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.seq = 0
        if servidor: self.socket.bind(self.endereco)

    def solicitar_conexao(self):
        try:
            self.socket.settimeout(5)
            self.socket.sendto(b'Conexao solicitada', self.endereco)
            print("Conexao solicitada")
            msg, addr = self.socket.recvfrom(1024)

            if msg == b'Conexao estabelecida':
                print("Conexao estabelecida")
                return True
            else:
                print("Conexao recusada")
                return False
        except timeout:
            print("Tempo de espera excedido")
            return False

    def esperar_conexao(self):
        while True:
            dado, addr = self.socket.recvfrom(1024)
            if dado == b'Conexao solicitada':
                print("Conexao solicitada")
                self.socket.sendto(b'Conexao estabelecida', addr)
                print("Conexao estabelecida")
                break

    def enviar(self, arquivo, addr=None):
        if addr is None:
            addr = self.endereco

        try:
            with open(arquivo, "rb") as arquivo:
                dado = arquivo.read(1024)
                while dado:
                    enviado = False
                    while not enviado:
                        mensagem = bytes([self.seq]) + dado
                        self.socket.sendto(mensagem, addr)
                        try:
                            ack, _ = self.socket.recvfrom(1024)
                            if ack == bytes([self.seq]):
                                enviado = True
                                print(f'ACK recebido {self.seq}')
                                self.seq = 1 - self.seq
                        except timeout:
                            print("Reenviando pacote...")
                    dado = arquivo.read(1024)
                self.socket.sendto(bytes([self.seq]) + b'--fim--', addr)
            print("Arquivo enviado!")
        except Exception as err:
            print(f"Erro: {err}")

    def receber(self, arquivo):
        addr = None
        with open(arquivo, 'wb') as arquivo:
            while True:
                dado, addr = self.socket.recvfrom(1024)
                seq, msg = dado[0], dado[1:]
                if msg == b'--fim--' and seq == self.seq:
                    break
                if seq == self.seq:
                    arquivo.write(msg)
                    self.socket.sendto(bytes([seq]), addr)
                    print(f'ACK enviado {seq}')
                    self.seq = 1 - self.seq
                else:
                    self.socket.sendto(bytes([1 - self.seq]), addr)

        print("Arquivo recebido!")
        return addr

    def encerrar(self):
        self.socket.close()
        print("Conexao encerrada")
