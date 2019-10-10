print('Exercício04 - Listas e Tuplas - DT de Nascimento')
meses=('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
nasc=input('Digite a Data de Nascimento no formato DD-MM-AAAA: ')

indice = int(nasc[3:5])-1
mes = meses[indice]

print('Você nasceu no mês de {}'.format(mes))
