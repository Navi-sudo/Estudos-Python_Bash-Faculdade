import requests
from bs4 import BeautifulSoup

url = 'https://www.fiap.com.br'

resposta = requests.get(url)

soup = BeautifulSoup(resposta.text, 'html.parser') #REMOVE HTML

texto = soup.get_text() #PEGAR SOMENTE TEXTO

palavras = texto.split() #QUEBRAR TEXTO EMM PALAVRAS

print(palavras)

with open('LIST.txt', 'w', encoding='utf-8') as arquivo: 
    arquivo.write(',\n'.join(palavras))  #SALVAR .TXT