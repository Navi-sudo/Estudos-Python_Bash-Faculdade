from ftplib import *

ftp = FTP('ftp.gnu.org')   
print(ftp.getwelcome()) #SABER QUE CONECTOU

usuario = input('Digite o usuario: ')
senha = input('Digite a senha: ')

ftp.login(usuario, senha)

print('Diretorio atual de trabalho: ', ftp.pwd())

ftp.cwd('pub') #PASTA "PUBLIC"

print('Diretório corrente: ', ftp.pwd())

print(ftp.retrlines('LIST')) #LISTA ARQUIVOS DA PASTA

ftp.quit()