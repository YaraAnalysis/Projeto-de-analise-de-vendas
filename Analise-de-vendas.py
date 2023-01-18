# Este projeto analisa as vendas de uma empresa com base nas informações dos arquivos da empresa.

import os
import pandas as pd

lista_arquivos = os.listdir("C:\Projetos-GIT\Projetos Mentoria\Projeto-de-analise-de-vendas\Vendas")
print(lista_arquivos)

tabela_total = pd.DataFrame()

for arquivo in lista_arquivos:
    if 'vendas' in arquivo.lower():
        #importar arquivo (por enquanto só imprimi)
        print(f'/content/drive/MyDrive/2. Curso Hashtag Treinamentos/Curso Básico de Python/Vendas/{arquivo}')

print(tabela_total)