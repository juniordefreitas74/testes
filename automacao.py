
import pyautogui
import time  # importar time
import pandas
# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 0.5  # Pausa de 0.5 segundos entre os comandos
# abrir o navegador (chrome)
pyautogui.press('win')

pyautogui.write('chrome')

pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')  # abrir nova aba


# entrar no link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(1.5)  # esperar 5 segundos para o site carregar

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.press('tab')

# escrever o seu email
pyautogui.write('jj@gmail.com')

pyautogui.press('tab')
pyautogui.write('********')
pyautogui.press('tab')
pyautogui.press('enter')

# Passo 3: Importar a base de produtos pra cadastrar
# importar a base de produtos
tabela = pandas.read_csv('produtos.csv', sep=',')
# print(tabela)  # printar a tabela de produtos
# print(tabela['Produto'])  # printar a coluna de produtos
# print(tabela['Preco'])  # printar a coluna de preços
# print(tabela['Quantidade'])  # printar a coluna de quantidade
# print(tabela['Fornecedor'])  # printar a coluna de fornecedores
# print(tabela['Produto'][0])  # printar o primeiro produto
# print(tabela['Preco'][0])  # printar o primeiro preço
# print(tabela['Quantidade'][0])  # printar a primeira quantidade
pyautogui.press('tab')
# Passo 4: Cadastrar um produto
for linha in tabela.index:  # para cada linha da tabela

    codigo = tabela.loc[linha, 'codigo']  # pegar o código do produto
    pyautogui.write(codigo)  # escrever o código do produto
    pyautogui.press('tab')  # pressionar tab para ir para o próximo campo

    marca = tabela.loc[linha, 'marca']  # pegar a marca do produto
    pyautogui.write(marca)  # escrever a marca do produto
    pyautogui.press('tab')  # pressionar tab para ir para o próximo campo

    tipo = tabela.loc[linha, 'tipo']  # pegar o tipo do produto
    pyautogui.write(tipo)  # escrever o tipo do produto
    pyautogui.press('tab')  # pressionar tab para ir para o próximo campo

    categoria = tabela.loc[linha, 'categoria']  # pegar a categoria do produto
    pyautogui.write(str(categoria))  # escrever a categoria do produto
    pyautogui.press('tab')  # pressionar tab para ir para o próximo campo
    # pegar o preço unitário do produto

    preco_unitario = tabela.loc[linha, 'preco_unitario']
    # escrever o preço unitário do produto
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')  # pressionar tab para ir para o próximo campo

    custo = tabela.loc[linha, 'custo']  # pegar o custo do produto
    pyautogui.write(str(custo))  # escrever o custo do produto
    pyautogui.press('tab')  # pressionar tab para ir para o próximo campo

    obs = tabela.loc[linha, 'obs']  # pegar a observação do produto
    if obs == 'nan':
        pyautogui.write(str(obs))  # escrever a observação do produto
    pyautogui.press('tab')  # pressionar tab para ir para o próximo campo
    pyautogui.press('enter')  # pressionar enter para cadastrar o produto

    pyautogui.scroll(5000)  # rolar a tela para cima
    pyautogui.click(x=160, y=241)
    pyautogui.press('tab')  # pressionar tab para ir para o próximo campo


# Passo 5: Repetir o processo de cadastro até o fim
