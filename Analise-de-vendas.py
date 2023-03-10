# Este projeto analisa as vendas de uma empresa com base nas informações dos arquivos da empresa.
import os
import pandas as pd

#importar arquivos
lista_arquivos = os.listdir("C:\Projetos-GIT\Projetos Mentoria\Projeto-de-analise-de-vendas\Vendas")

tabela_total = pd.DataFrame()

#criar um arquivo único
for arquivo in lista_arquivos:
    if 'vendas' in arquivo.lower():
        tabela = pd.read_csv(f'C:\Projetos-GIT\Projetos Mentoria\Projeto-de-analise-de-vendas\Vendas\{arquivo}')
        tabela_total = tabela_total.append(tabela)

print(tabela_total)

#Cálculo do produto mais vendido
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
print('\nProdutos mais vendidos')
print(tabela_produtos)

#Cálculo do produto com maior faturamento
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)

print('\nProdutos com maior faturamento')
print(tabela_faturamento)

#Cálculo da loja/cidade que mais vendeu (em faturamento)
tabela_loja = tabela_total.groupby('Loja').sum()
tabela_loja = tabela_loja[['Faturamento']].sort_values(by='Faturamento', ascending=False)

print('\nLojas com maior faturamento')
print(tabela_loja)
