Parte 1 do projeto da disciplina de Infraestrutura de Comunicação.

Grupo: Filipe Eduardo Ferreira da Silva, Gabriel jatoba Campos Marques dos Santos, Tomás Nascimento Santos, Yasmim Adrieny da Silva Sales

O objetivo da entrega é implementar comunicação UDP usando a biblioteca de Pyhon,Socket,para enviar e devolver
2 arquivos(um de imagem e um de texto)

Essa parte tem 2 pastas, uma com arquivos que vão compor a atuação de um cliente ,e outra a de um servidor.

Na pasta client encontram-se o código do fonte (arquivo de terminação .py) que simula a atuação do cliente ,a imagem e o texto que serão enviados.

Na pasta server encontra-se o arquivo .py que atua como servidor

Para executar a entrega,abra dois terminais nas pastas client e server e rode os seguintes comandos:
python client.py
python server.py

Tanto o código do servidor quanto o do cliente, possuem 2 funções uma de envio de arquivo e outra de recebimento, que são chamadas quando conveniente para o funcionamento do código. Nessa segunda entrega, temos a verificação do ACK que faz a verificação a cada pacote de 124 bits enviados.

Se tudo funcionar,os prints para checagem de recebimento e envio dos arquivos que estão no código devem aparecer.
