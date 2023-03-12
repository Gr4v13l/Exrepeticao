#para descobrir i fator de um num usamos *=
num = int(input('Insira um núemro para descobrir seu fatorial '))

fatorial = 1
for i in range (num, num+1):
  fatorial *= i

print('O fatorial é: ', fatorial) 