print('Exercicio 03 - Média Ponderada')
nota1 = float(input('Digite a Nota1: '))
peso1 = float(input('Digite o peso da Nota1: '))
nota2 = float(input('Digite a Nota2: '))
peso2 = float(input('Digite o peso da Nota2: '))

media = ((nota1*peso1) + (nota2*peso2))/(peso1+peso2)
print('A média ponderada do aluno é {}'.format(media))
