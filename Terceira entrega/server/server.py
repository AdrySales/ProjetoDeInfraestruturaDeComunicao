import sys
import os

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)

from socket import *
from rdt import RDT
from handler import Handler

servidor = RDT(servidor = True)
handler = Handler()

while True:
  msg, addr = servidor.receber()
  
  print(f"Recebido: {msg} de {addr}")
  
  data = msg.split(",")
  comando = data[0]

  if comando == "conectar":
    endereco = f"{addr[0]}:{addr[1]}"

    print(data[1], endereco)
    usuario = handler.conectar_usuario(data[1], endereco)
    print(f"Usuário conectado: {usuario}")
    servidor.enviar(usuario[1], addr)
  
  elif comando == "encerrar":
    print(f"Conexão com {addr} encerrada")
    resposta = handler.desconectarUser(data[1])
    servidor.enviar(resposta, addr)

  elif comando == "reservar":
    resposta = handler.fazerReserva(data[1],data[2],data[3],data[4])
    servidor.enviar(resposta, addr)

  elif comando == "cancelar":
    resposta = handler.cancelarReserva(data[1],data[2],data[3],data[4])
    servidor.enviar(resposta, addr)

  elif comando =="verificar":
    resposta = handler.verificarDisponibilidade(data[1],data[2])
    servidor.enviar(resposta,addr)
    
  elif comando =="listar":
    resposta = handler.listar_usuarios()
    servidor.enviar(resposta,addr)
