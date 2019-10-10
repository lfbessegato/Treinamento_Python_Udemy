## for loop range
##for i in range(0,10):
##   print(i)


## for loop aninhado
##compras = [['Arroz', 'Feijão', 'Macarrão'],['Carne','Frango','Peixe'],['Leite','Yougurte']]
##
##for i in compras:
##    for item in i:
##        print(item)

## for loop com dicionários
##cores = {'verde':'green','preto':'black','azul':'blue'}
##for i in cores:
##    print(i,':',cores[i])


## Somatório com for loop
##vendas = [1000,450,300,920,600]
##total = 0
##for i in vendas:
##    total += i
##    print(total)
##print (total)

## loop for com listas e Strings
##compras = ['Arroz', 'Feijão', 'Macarrão', 'Carne']
##nome = 'Luciano'
##for i in compras:
##   print(i)
##
##for i in nome:
##   print (i)


## exemplo de loop while
##x = 0
##pessoas = []
##while x < 4:
##    nome = input('Qual o seu Nome? ')
##    ## Evitar que o nome joao seja acrescentado à Lista
##    if nome == 'joao':
##    ## continue (sai do teste e continue no Loop)
##       break 
##    pessoas.append(nome)
##    x += 1
##    
##print(pessoas)
