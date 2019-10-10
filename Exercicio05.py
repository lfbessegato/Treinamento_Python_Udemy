print('Exercício05 - Dicionário de Cores')
cores={'verde':'Green','amarelo':'Yellow','azul':'Blue','vermelho':'Red','preto':'Black'}
cor=input('Digite a Cor para traduzir: ').lower()
traducao = cores.get(cor,'Esta informação não consta no dicionário')
print(traducao)
