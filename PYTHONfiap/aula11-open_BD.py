basedados = []
with open('iris-open_BD.data', 'r') as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(','))
print(basedados)

print(basedados[0][0])