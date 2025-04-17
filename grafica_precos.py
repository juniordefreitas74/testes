import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import math

tabelinha = []
site = requests.get(
    'https://www.futuraim.com.br/produto/cartao-de-visita-em-couche-brilho?id=4527')
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


titulo = dados_pagina.find_all('div', class_="col-md-6")
# print(titulo)
for div3 in titulo:
    # print(div3)
    filtro4 = div3.find('p', class_="font-small")
    if filtro4:
       # print(filtro4)
        texto_filtro2 = div3.get_text(strip=True)
        parte = texto_filtro2[:88]

        print(f'\n{parte}\n')


for texto_filtro, texto_preco in zip(lista_qtd, lista_preco):
    # adiciona os valores na lista tabelinha
    tabelinha.append((texto_filtro, texto_preco))
    # print(tabela)
for item in tabelinha:
    # replce revove o R$ e a virgula e atribui o ponto
    custo = float(item[1].replace('R$', '').replace(',', '.'))
    venda = (custo*1.66)
    # imprime os valores da lista tabelinha
    print(
        f'Custo= {item[0]} : R$ {custo:.2f} \nPreço de venda: {item[0]} = R$ {venda:.2f} ', '\n')
