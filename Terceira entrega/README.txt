Parte 3 do projeto da disciplina de Infraestrutura de Comunicação.

Grupo: Filipe Eduardo Ferreira da Silva, Gabriel jatoba Campos Marques dos Santos, Tomás Nascimento Santos, Yasmim Adrieny da Silva Sales

O objetivo da entrega é implementar um Sistema de gerenciamento de reservas de salas com paradigma cliente-servidor,funcionando com mais de um cliente e usando transmissão confiável(na camada de aplicação)


Essa parte tem 2 pastas, uma com arquivos que vão compor a atuação de um cliente ,e outra a de um servidor.

Na pasta client encontra-se o código do fonte (arquivo de terminação .py) que simula a atuação do cliente ,onde ele escolhe as opções possíveis de interação com o servidor que foram especificadas nas orientações do projetoprint(Conectar ao aplicativo;Listar usuários conectados;Reservar uma sala;Cancelar uma reserva;Verificar disponibilidade em sala específica ; Sair do aplicativo)


Na pasta server encontram-se 2 arquivos .py que atuam como servidor,um onde as funções responsáveis pelas interações acima são implementadas(handler) e um que se comunica com primeiro para chamar essas funções quando necessário(server).
Também tem arquivos .csv que armazenam os usuários conectados e salas(ambos vão sofrer alterações devido ao funcionamento do Sistema)


Para executar a entrega,abra terminais nas pastas client e server e rode os seguintes comandos(faça o de criar o client em mais de 1 terminal,para provar que o sistema funciona com 2 ou mais clientes):
python client.py
python server.py


Se tudo funcionar,o servidor e clients gerarão as alterações esperadas no terminal.
