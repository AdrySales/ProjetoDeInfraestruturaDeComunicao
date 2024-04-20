from socket import *
import csv
import os
class Handler:
    
  def conectar_usuario(self, nome, endereco):
    print(nome, endereco)

    with open("usuarios.csv", "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_data = line.strip().split(",")
        if user_data[1] == nome:
            print('Usuário encontrado')
            user_data[3] = "True"
            if user_data[2] == endereco:
                lines[i] = ",".join(user_data) + "\n"
            else:
                user_data[2] = endereco
                lines[i] = ",".join(user_data) + "\n"
            with open("usuarios.csv", "w") as file:
                file.writelines(lines)
            return user_data

    last_id = 0
    if len(lines) > 1:
        last_line = lines[-1].strip()
        last_id = int(last_line.split(",")[0])

    user_data = [last_id + 1, nome, endereco, "True"]
    with open("usuarios.csv", "a") as file:
        file.write(f"\n{last_id + 1},{nome},{endereco},True")

    return user_data



  def checarReserva(self,room, day, time,person_id):
          with open('reservas.csv', 'r') as file:
              reader = csv.reader(file)
              next(reader)  # Pula a primeira linha
              for row in reader:
                if len(row) >= 4 and row[1] == room and row[2] == day and row[3] == time and row[0] == person_id:
                      return False
          return True

  def fazerReserva(self,room,day,time,person_id):
        if self.checarReserva(room,day,time,person_id):
            with open('reservas.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([person_id,room, day, time])
                file.write(os.linesep) 
            retorno="Reserva feita com sucesso!"
            print(retorno)
            return retorno
        else:
            retorno="Erro: A sala já está reservada nesse horário."
            print(retorno)
            return retorno




  def cancelarReserva(self, room, day, time, person_id):
    reservas = []
    reserva_encontrada = False

    # Ler as reservas do arquivo CSV, ignorando a primeira linha
    with open('reservas.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula a primeira linha
        for row in reader:
            if len(row) >= 4 and row[1] == room and row[2] == day and row[3] == time and row[0] == person_id:
                reserva_encontrada = True
            else:
                reservas.append(row)

    # Escrever as reservas atualizadas no arquivo CSV
    with open('reservas.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reservas)

    if reserva_encontrada:
        retorno= "Reserva cancelada com sucesso!"
        print(retorno)
        return retorno
    else:
        retorno ="Erro: Reserva não encontrada ou não pertence a este usuário."
        print(retorno)
        return retorno
  
  def listar_usuarios(self):###########tentativa:criar a lista de usuarios ativos
    usuarios = []

    with open("usuarios.csv", "r") as file:
      lines = file.readlines()
      for line in lines:
        user_data = line.strip().split(",")
        if user_data[3] == "True":
         usuarios.append(user_data[1])
    retorno = ",".join(usuarios)
    print(retorno)
    return ",".join(usuarios)
  

  def verificarDisponibilidade(self,sala, dia):
    
    horarios_padrao = ["06:00", "07:00", "08:00","09:00",  "10:00", "11:00", "12:00","13:00","14:00",   "15:00", "17:00"]


    horarios_reservados = []

  
    with open('reservas.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            if len(row) >= 4 and row[1] == sala and row[2].lower() == dia.lower():  
                horarios_reservados.append(row[3])  

    
    horarios_disponiveis = [hora for hora in horarios_padrao if hora not in horarios_reservados]

   
    disponibilidade = f"{sala} {dia[:3]} -> {' '.join(horarios_disponiveis)}"
    
    return disponibilidade

  


  def desconectarUser(self, nome):
      
      found = False

      with open("usuarios.csv", "r") as file:
          reader = csv.reader(file)
          lines = list(reader)

      for line in lines:
          if line[1] == nome:
              line[3] = "False"  # Altera o campo "ativo" para "false"
              found = True

      if found:
          with open("usuarios.csv", "w", newline='') as file:
              writer = csv.writer(file)
              writer.writerows(lines)
          print(f"Usuário {nome} desconectado com sucesso.")
          return "Usuário desconectado com sucesso"
      else:
          print(f"Usuário {nome} não encontrado.")
          return "Usuário não encontrado"
