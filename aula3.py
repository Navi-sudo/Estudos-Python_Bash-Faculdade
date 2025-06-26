pontos = int(input('Informe o número de pontos do cliente: '))
if pontos >= 1000:
    print('O cliente recebe 3GB de bônus.')
elif pontos > 500:
    print('O cliente recebe 1.5GB de bônus.')
elif pontos > 200:
    print('O cliente recebe 500MB de bônus.')
else:
    print('O cliente recebe 200MB de bônus.')