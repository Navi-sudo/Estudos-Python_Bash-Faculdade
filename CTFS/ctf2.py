with open('us-counties.csv', 'r') as arquivo:
    count = 0 
    cases = 0
    for linha in arquivo:
        data = linha.split(',')
        if '2020-09-27' == data[0]:
            cases = cases + int(data[4])
            count += 1
            print(data)
    print(f'QTD {count} | casos: {cases}' )