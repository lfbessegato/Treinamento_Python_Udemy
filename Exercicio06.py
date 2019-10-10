print ('Exercício06 - Média do Aluno')
nome = input('Digite o nome do Aluno: ').upper()
CHGeral = 20

## Validar o valor das Notas
valida_nota = False
while valida_nota == False:
   nota1 = input('Digite a nota da Prova 1: ')
   try:
      nota1 = float(nota1)

      if nota1 > 10 or nota1 < 0:
         print ("Nota inválida. Valor deve ser entre 0 e 10.")
      else:
         valida_nota = True
   except: 
      print ("Nota Inválida. Use apenas números e separe os decimais com ponto.'.'.")

valida_nota = False
while valida_nota == False:
   nota2 = input('Digite a nota da Prova 2: ')
   try:
      nota2 = float(nota2)

      if nota2 > 10 or nota2 < 0:
         print ("Nota inválida. Valor deve ser entre 0 e 10.")
      else:
         valida_nota = True
   except: 
      print ("Nota Inválida. Use apenas números e separe os decimais com ponto.'.'.")

## Validar o número de Faltas
valida_faltas = False
while valida_faltas == False:
   faltas = input('Digite o Total de Faltas: ')
   try:
      faltas = float(faltas)

      if faltas > 20 or faltas < 0:
         print ("O Número de Faltas inválido. Valor precisa ser entre 0 e 20.")
      else:
         valida_faltas = True

   except: 
      print ("Número de Faltas Inválido. Use apenas números e separe os decimais com ponto.'.'.")


presenca = (((CHGeral - faltas)/CHGeral)*100)
media = (nota1 + nota2)/2

if media >= 6 and presenca >= 70:
   resultado = 'APROVADO'

elif media < 6 and presenca < 70:
   resultado = 'REPROVADO por média e por faltas'

elif media < 6:
   resultado = 'REPROVADO por média'

elif presenca < 70:
   resultado = 'REPROVADO por faltas'
   
else:
    print ('ERRO')

print ('Nome: {}'.format(nome))
print ('Média: {}'.format(media))
print ('Presença: {}%'.format(presenca))
print ('Resultado: {}'.format(resultado))

   


              
