idade = input('Quantos anos você tem? ')

if idade.isdigit():
    idade = int(idade)
    if idade < 18:
        print('Acesso Negado. Somente maiores de 18 anos.')
    else:
        print('Bem vindo.')
else:
    print('Tipo de dado inválido.')