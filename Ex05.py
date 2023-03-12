import random

a = int(input('Insira quantas vezes você deseja jogar a moeda: '))
n_cara = 0
n_coroa = 0


for i in range(a):
 resultado = random.randint(0, 1)
 
 if resultado == 0:
    print('Coroa')
    n_coroa +=1 
 else:
    print('Cara')
    n_cara +=1

print('Número de coroa: ', n_coroa)
print('Número de cara: ', n_cara) 



 
