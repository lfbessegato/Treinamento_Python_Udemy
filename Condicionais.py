print('Condicionais - If/Elif/Else')
idade = int(input('Digite a sua idade: '))
sexo = input('Digite o sexo M ou F: ').lower()
cidade = input('Digite a cidade: ').lower()

if cidade == 'rio' or cidade == 'sao paulo':

          if sexo == 'm':
              if idade < 18:
                 print ('Homem menor de idade, da região sudeste')
              else:
                 print ('Homem maior de idade, da região sudeste')

          elif sexo == 'f':
               if idade < 18:
                  print ('Mulher menor de idade, da região sudeste')
               else:
                  print ('Mulher maior de idade, da região sudeste')

else:
   print ('Teste apenas para região sudeste')
