import requests
import time

domain = 'fiap.com.br' #DOMINIO ATACADO

with open('aula19-subdominios.txt', 'r') as sub_file: #SALVA EM TXT SUBDOMINIOS
    subdomains = sub_file.read().splitlines() #QUEBRA E MAPEIA LINHAS GERANDO LISTAS

with open('aula19-arquivos.txt', 'r') as url_file: #SALVA EM TXT ARQUIVOS E DIRETORIOS
    urls = url_file.read().splitlines()

for subdomain in subdomains: #PERCORRE SUBDIRETÓRIO POR SUBDIRETÓRIO
    for url in urls: #PERCORRE URL POR URL
        if url.startswith('http'): #PARAMETRO PARA ADICIONAR A "INICIAL" E DESCOBRIR SE O ENDEREÇO É VALIDO
            full_url = url
        elif url.startswith('/'):
            full_url =  f'http://{subdomain}.{domain}{url}' # DOMINIO > SITE ESCOLHEDO - SUBDOMINIO > SUBDOMINIO.TXT > URL - ARQUIVOS.TXT >
        else:
            full_url = f'http://{subdomain}.{domain}/{url}' #ADICION AO / PARA URL COMPLETA
        
        try:  #CONDIÇÃO PARA TESTAR URL
            response = requests.get(full_url)
            if response.status_code == 200: # VERIFICA SE O CODIGO RETORNADO É 200 > 200 = EXISTE
                print(f'A URL {full_url} existe.')
            else: 
                print(f'A URL {full_url} existe, mas retornou o código de statys {response.status_code}.') 
        except requests.exceptions.RequestException:
            print(f'A URL {full_url} não existe.') 