print('Exercício 09 - IMC')

def imc(peso,altura):
    imc = peso / (altura * altura)
    return (imc)

def class_imc(sexo, peso, altura):
    valor_imc = imc(peso, altura)      

    if sexo == 'f':
       if valor_imc < 19.1:
            return 'Abaixo do Peso'
       elif valor_imc >= 19.1 and valor_imc < 25.8:
            return 'Peso normal'
       elif valor_imc >= 25.8 and valor_imc < 27.3:
            return 'Marginalmente acima do peso'
       elif valor_imc >= 27.3 and valor_imc < 32.3:
            return 'Acima do peso ideal'
       elif valor_imc >= 32.3:
            return 'Obeso'
       else:
            print ('Erro de Cálculo. Entre em contato com o Administrador.')
          
    elif sexo == 'm':
       if valor_imc < 20.7:
            return 'Abaixo do Peso'
       elif valor_imc >= 20.7 and valor_imc < 26.4:
            return 'Peso normal'
       elif valor_imc >= 26.4 and valor_imc < 27.8:
            return 'Marginalmente acima do peso'
       elif valor_imc >= 27.8 and valor_imc < 31.1:
            return 'Acima do peso ideal'
       elif valor_imc >= 31.1:
            return 'Obeso'
       else:
            print ('Erro de Cálculo. Entre em contato com o Administrador.')

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
v_imc = imc(peso,altura)
c_imc = class_imc(sexo,peso,altura)

print ('O seu IMC é: {:.2f}'.format(v_imc))
print ('A sua classificação é: {}'.format(c_imc)) 




