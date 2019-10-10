print('Exercicio 09 - Módulos')
import time as t
import matplotlib.pyplot as plt
tempos = []
vezes = []
legenda = []
vez = 1
repet = 6
print ('Este programa marcará o tempo gasto para digitar a palavra GETULINA.Você terá que digitar-la '+str(repet)+ ' vezes.')
input ('Aperte <ENTER> para começar')


while vez <= repet:
    inicio = t.clock()
    input ('Digite a palavra: ')
    final = t.clock()
    tempo = round(final - inicio,2)
    tempos.append(tempo)
    vezes.append(vez)
    vezstr = str(vez)+'a vez'
    legenda.append(vezstr)
    vez += 1
    
plt.xticks(vezes,legenda)
plt.plot(vezes,tempos)
plt.show()
