"""
Instruções em
<!-- github.com/Botjak -->
"""
import datetime
data_atual = datetime.datetime.today()

arquivos = 0
# Limpador de repetições
clean_dados = open('dados.txt', 'r').readlines()
clean_dados2 = set(clean_dados)
cleandata = open(f'resultado {data_atual.strftime("%d %B %Y às %H;%M%p")}.txt', 'w')

for line in clean_dados2:
    arquivos += 1
    cleandata.write(line)

quantidade = clean_dados
carregados = len(quantidade)
totalagora = len(quantidade) - arquivos
print(f'Quantidade carregado:           [{carregados}]')
print(f'Total limpado:                  [{totalagora}]')
print(f'Arquivos não duplicados:        [{arquivos-1}]')
print('Limpado com sucesso!, mais rápido que o FLASH!')
