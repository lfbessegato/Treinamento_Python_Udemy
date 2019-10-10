import func

print('Vamos calcular o seu imc?')

valida_sexo = False
while valida_sexo == False:       
      sexo = input('Digite o seu Sexo: (F ou M): ').lower()
      if sexo != 'm' and sexo != 'f':
         print ('Sexo Inválido. Digite M ou F.')
      else:
         valida_sexo = True
         print('\n')
         
valida_peso = False
while valida_peso == False:
    peso = input('Digite o peso em KG: ')
    try:
      peso = float(peso)
      if peso <= 0: 
         print('O Peso Inválido. Número não pode ser zero ou negativo.')
      else:
         valida_peso = True
         print('\n')
    except:
      print('Peso Inválido. Use apenas número e separe decimais com ponto.')


valida_altura = False
while valida_altura == False:
    altura = input('Digite a altura em metros: ')
    try:
      altura = float(altura)
      if altura <= 0: 
         print('A Altura Inválida. Número não pode ser zero ou negativo.')
      else:
         valida_altura = True
         print('\n')
    except:
      print('Altura Inválida. Use apenas número e separe decimais com ponto.')

## Chamada das Funções
v_imc = func.imc(peso,altura)
c_imc = func.class_imc(sexo,peso,altura)

print ('O seu IMC é: {:.2f}'.format(v_imc))
print ('A sua classificação é: {}'.format(c_imc)) 




