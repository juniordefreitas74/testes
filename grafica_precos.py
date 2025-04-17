import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import math

tabelinha = []
site = requests.get(
    'https://www.futuraim.com.br/produto/cartao-de-visita-em-couche-brilho?id=4527#')
dados_pagina = BeautifulSoup(site.text, 'html.parser')

# PROCURA TODOS DIVS DA PAGINA QUE CONTENHAM A CLASSE form-check
quantidade = dados_pagina.find_all('div', class_='form-check')
lista_qtd = []

for div in quantidade:
    filtro = div.find('input', class_='mr-2')
    if filtro:
        # print(filtro)
        texto_filtro = div.get_text(strip=True)
        # print(texto_filtro)
        lista_qtd.append(texto_filtro)
    # print(div)

preco = dados_pagina.find_all('label', class_="mb-0")
lista_preco = []

for div2 in preco:
    # print(div2)
    texto_preco = div2.get_text(strip=True)
    # print(texto_preco)
    lista_preco.append(texto_preco)
# coloca os valores de texto_filtro e texto_preco em uma lista
for texto_filtro, texto_preco in zip(lista_qtd, lista_preco):
    # adiciona os valores na lista tabelinha
    tabelinha.append((texto_filtro, texto_preco))
    # print(tabela)
for item in tabelinha:
    # replce revove o R$ e a virgula e atribui o ponto
    venda = float(item[1].replace('R$', '').replace(',', '.'))
    # imprime os valores da lista tabelinha
    print(f'Custo= {item[0]} : {item[1]} \nPreço de venda: {item[0]} = R$ {venda * 1.66:.2f} ','\n')
