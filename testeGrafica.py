import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Lê as URLs do arquivo
with open('lista_cartoes_futura.txt', 'r') as file:
    urls = [linha.strip() for linha in file if linha.strip()]

# Cria o objeto ExcelWriter para salvar várias abas
with pd.ExcelWriter('cartoes_futura.xlsx', engine='openpyxl') as writer:

    for url in urls:
        try:
            site = requests.get(url)
            dados_pagina = BeautifulSoup(site.text, 'html.parser')

            # Extrai título da aba e faz limpeza
            titulo_tag = dados_pagina.find('title')
            nome_bruto = titulo_tag.text if titulo_tag else 'Produto'

            # Limpa o nome da aba: remove palavras comuns e caracteres indesejados
            nome_limpo = re.sub(
                r'(Cart(ão|ao)?( de)? Visita|em|com|para|personalizado|duplo)', '', nome_bruto, flags=re.IGNORECASE)
            nome_limpo = re.sub(r'[^a-zA-Z0-9 ]', '', nome_limpo)
            nome_limpo = "_".join(nome_limpo.strip().split())[:31]

            # Extrai quantidades
            quantidade = dados_pagina.find_all('div', class_='form-check')
            lista_qtd = [div.get_text(strip=True) for div in quantidade if div.find(
                'input', class_='mr-2')]

            # Extrai preços
            preco = dados_pagina.find_all('label', class_="mb-0")
            lista_preco = [div.get_text(strip=True) for div in preco]

            # Monta a tabelinha
            tabelinha = []
            for texto_filtro, texto_preco in zip(lista_qtd, lista_preco):
                custo = float(texto_preco.replace('R$', '').replace(',', '.'))
                venda = round(custo * 1.66, 2)
                tabelinha.append([texto_filtro, custo, venda])

            # Cria o DataFrame
            df = pd.DataFrame(tabelinha, columns=[
                              'Descrição', 'Custo (R$)', 'Venda (R$)'])

            # Escreve a aba
            df.to_excel(writer, sheet_name=nome_limpo, index=False)

            print(f'✅ Processado: {nome_limpo}')

        except Exception as e:
            print(f'❌ Erro ao processar {url}: {e}')
