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

