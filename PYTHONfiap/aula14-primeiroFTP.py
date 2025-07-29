#BIBLIOTECA FTPLIB
# COMUNICAÇÃO/TRANSFERENCIA DE ARQUIVOS SEM SE PREOCUPAR COM EXIBIÇÃO DE TELA
# PASTA PC X >>>> PASTA PC Y


from ftplib import *

ftp = FTP('ftp.gnu.org') #dominio

print(ftp.getwelcome())

ftp.quit()

#FUNCIONOU >> '220 ProFTPD Server'
#Significa que se conectou com sucesso e pode transferir as informações.