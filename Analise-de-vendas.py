# Este projeto analisa as vendas de uma empresa com base nas informações dos arquivos da empresa.

import os
import pandas as pd

lista_arquivos = os.listdir("C:\Projetos-GIT\Projetos Mentoria\Projeto-de-analise-de-vendas\Vendas")
print('\nLista de Arquivos: \n{}'.format(lista_arquivos))

tabela_total = pd.DataFrame()

for arquivo in lista_arquivos:
    if 'vendas' in arquivo.lower():
        #importar arquivo (por enquanto só imprimi)
        tabela = pd.read_csv(f'C:\Projetos-GIT\Projetos Mentoria\Projeto-de-analise-de-vendas\Vendas\{arquivo}')
        tabela_total = tabela_total.append(tabela)
        #print(f'C:\Projetos-GIT\Projetos Mentoria\Projeto-de-analise-de-vendas\Vendas{arquivo}')

print(tabela_total)

#Cálculo do produto mais vendido
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
print('\nProdutos mais vendidos')
print(tabela_produtos)

#Cálculo do produtot com maior faturamento
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)

print('\nProdutos com maior faturamento')
print(tabela_faturamento)