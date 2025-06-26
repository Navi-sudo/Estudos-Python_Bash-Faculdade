from aula10_funcoes_uteis import *

usuarios={}
opcao = perguntas()

while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        inserir(usuarios)
    opcao = perguntas()
