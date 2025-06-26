top3 = ['Porquinho', 'Camelo', 'Plankton']

print('Top imitações do ursinho: \n')
#print(top3)

for top in top3:
    print(top)

top3.append(input('Adicione uma imitação ao top: '))

print('Top *atualizado* imitações do ursinho: \n')

for top in top3:
    print(top)