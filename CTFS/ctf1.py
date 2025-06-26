with open('us-counties.csv', 'r') as arquivo:
    count = 0 
    for linha in arquivo:
        data = linha.split(',')
        if '2021-09-27' == data[0]:
            count += 1
            print(data)
    print(f'QTD {count}')