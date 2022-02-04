from sys import displayhook
import pandas as pd

_excel = pd.read_excel('Template_exportacao_dados-v2.xlsx')
dic = dict(_excel)

cabecalho = ['insert into tabela values (']
dados = []

for key, value in dic.items():
    cabecalho.append(f'{key}')
    # dados.append(f'{value}')

cabecalho.insert(len(cabecalho), ') values ')

print(cabecalho)
# print(dic)
# print(_excel)
# displayhook(pd)
