import sys
import os
import signal
import time

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)

from socket import *
from rdt import RDT

cliente = RDT()

def interromper_programa(signal, frame):
	print("\nSaindo do aplicativo...")
	cliente.encerrar()
	sys.exit(0)

signal.signal(signal.SIGINT, interromper_programa)

def menu():
	usuario = None

	while True:
		print("\n===============================")
		print("\nMenu:")
		print("\nEscolha uma opção:")
		print("1. Conectar ao aplicativo")
		print("2. Listar usuários conectados")
		print("3. Reservar uma sala")
		print("4. Cancelar uma reserva")
		print("5. Verificar disponibilidade em sala específica")
		print("6. Sair do aplicativo")
		print("\n===============================")

		opcao = input("Digite o número da opção desejada: ")

		if opcao == "1":
				if usuario:
					print('Usuário já conectado!')
					time.sleep(2)

				else:
					print("Por favor informe seus dados: ")
					
					nome = input("Nome: ")
					
					cliente.enviar(f"conectar,{nome}")
					usuario = cliente.receber()

					if usuario:
						print(f"Usuário conectado: {usuario[0]}")
						time.sleep(2)

		elif opcao == "2":
				if not usuario:
					print('Usuário não conectado!')
					time.sleep(2)

				else:
					cliente.enviar("listar")
					#print("Usuários conectados: " + cliente.receber())
					estao_online = cliente.receber()
					print("Usuários conectados: ")
					print(estao_online)

		elif opcao == "3":
				if not usuario:
					print('Usuário não conectado!')
					time.sleep(2)

				else:
					print('________________Reserva de salas__________________________')
					print('As salas que podem ser alugadas são as  E101 até E105')
					print('O modelo de data é: 00/00/0000 e o de horas é 00:00')
					print('Por favor informar o código recebido no ato do cadastro!')
					print('__________________________________________________________')

					sala=input('Informe a sala que deseja reservar:')
					dia=input('Informe o dia que deseja reservar:')
					horario=input('Informe o horário que deseja reservar:')
					id=input('Informe o ID da pessoa que deseja reservar:')
					cliente.enviar(f"reservar,{sala},{dia},{horario},{id}")
					usuario = cliente.receber()
					print(usuario)

					if usuario:
						print(f"Usuário conectado: {usuario[0]}")
						time.sleep(2)

		elif opcao == "4":
				if not usuario:
					print('Usuário não conectado!')
					time.sleep(2)

				else:
					sala=input('Informe a sala que deseja cancelar:')
					dia=input('Informe o dia que deseja cancelar:')
					horario=input('Informe o horário que deseja cancelar:')
					id=input('Informe o ID da pessoa que deseja cancelar:')
					cliente.enviar(f"cancelar,{sala},{dia},{horario},{id}")
					usuario = cliente.receber()
					print(usuario)

		elif opcao == "5":
				if not usuario:
					print('Usuário não conectado!')
					time.sleep(2)

				else:
					sala=input('Informe a sala que deseja verificar:')
					dia=input('Informe o dia que deseja verificar:')
					cliente.enviar("verificar,"+sala+","+dia)
					usuario=cliente.receber()
					print("Os horarios dipoíveis são:")
					print(usuario)
		elif opcao == "6":
				nome=input("Digite seu nome:")
				cliente.enviar(f'encerrar,{nome}')
				print(cliente.receber())
				cliente.encerrar()
				break

		else:
				print("Opção inválida. Por favor, escolha uma opção válida.")  

menu()