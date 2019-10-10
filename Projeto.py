print ('Projeto - Média do Aluno')
import matplotlib.pyplot as plt
nome = input('Digite o nome do Aluno: ').upper()
CHGeral = 40
geral = [0,1,2,3,4,5,6,7,8,9,10]
notas = []

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
      
valida_nota = False
while valida_nota == False:
   nota3 = input('Digite a nota da Prova 3: ')
   try:
      nota3 = float(nota3)

      if nota3 > 10 or nota3 < 0:
         print ("Nota inválida. Valor deve ser entre 0 e 10.")
      else:
         valida_nota = True
   except: 
      print ("Nota Inválida. Use apenas números e separe os decimais com ponto.'.'.")

valida_nota = False
while valida_nota == False:
   nota4 = input('Digite a nota da Prova 4: ')
   try:
      nota4 = float(nota4)

      if nota4 > 10 or nota4 < 0:
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

      if faltas > 40 or faltas < 0:
         print ("O Número de Faltas inválido. Valor precisa ser entre 0 e 40.")
      else:
         valida_faltas = True

   except: 
      print ("Número de Faltas Inválido. Use apenas números e separe os decimais com ponto.'.'.")


presenca = (((CHGeral - faltas)/CHGeral)*100)

media = (nota1 + nota2 + nota3 + nota4)/4

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

notas = [nota1,nota2,nota3,nota4]

plt.plot(geral,notas)
plt.show()


              
