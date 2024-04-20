import sys
import os

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)

from socket import *
from rdt import RDT

servidor = RDT(servidor = True)

servidor.esperar_conexao()

addr = servidor.receber("recebido.png")
servidor.enviar("recebido.png", addr)  

servidor.receber("recebido.txt")
servidor.enviar("recebido.txt", addr)  
servidor.encerrar()