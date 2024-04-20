
import sys
import os

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)

from socket import *
from rdt import RDT

cliente = RDT()

while True:
    conexao_estabelecida = cliente.solicitar_conexao()
    if conexao_estabelecida: break

cliente.enviar("teste.png")
cliente.receber("arquivoRecebido.png")

cliente.enviar("teste.txt")
cliente.receber("arquivoRecebido.txt")
cliente.encerrar()
