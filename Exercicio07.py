print('Exercício07 - Fatura')
resposta = 's'
fatura = []
total = 0
valida_preco = False

while resposta == 's':
   produto = input('Digite o nome do produto: ')

   while valida_preco == False:
      preco = input('Qual o preço do produto? ')
      try:
         preco = float(preco)

         if preco <= 0:
            print("O Preço precisa ser maior que zero")
         else:
            valida_preco = True
            
      except:
         print("Formato de preço inválido. Use apenas números e separe os centavos com '.'.")

   
   fatura.append([produto,preco])
   total += preco
   valida_preco = False
   resposta = input('Deseja comprar mais algum produto? (S ou N): ').lower()

print ('### Produtos Adiquiridos ###')
for i in fatura:
   print(i[0], ' - R$: ', i[1])
   
print('O total da fatura é R$ {:.2f}'.format(total))
