#primeiro definir as variaveis
votos_cand1 = 0
votos_cand2 = 0
votos_cand3 = 0
votos_brancos = 0
votos_nulos = 0

while True:
 print('Escolha entre as opcões abaixo: \n 1. Candidato Jair Rodrigues \n 2. Candidato Carlos Luz \n 3. Candidato Neves Rocha \n 4. Nulo \n 5. Branco \n 6. Resultados')
 voto = int(input('Entre com seu voto: '))

 if voto == 1:
  votos_cand1 +=1
 elif voto ==2:
  votos_cand2 +=1
 elif voto == 3:
  votos_cand3 +=1
 elif voto == 4:
  votos_brancos +=1
 elif voto == 5:
  votos_nulos =+1
 elif voto == 6:
  #calculos
  total_votos = votos_cand1 + votos_cand2 + votos_cand3 + votos_brancos + votos_nulos
  #porcentagem de votos nulos: votos nulos/ total de votos e *100 para porcentagem
  porcentagem_nulos = (votos_nulos / total_votos)*100
  #porcentagem de brancos segue a mesma lógica
  porcentagem_brancos = (votos_brancos/total_votos)*100

  print('O candidato Jair Rodrigues recebeu ', votos_cand1, ' votos.')
  print('O candidato Carlos Luz recebeu ', votos_cand2, ' votos.')
  print('O candidato Neves Rocha recebeu ', votos_cand3, ' votos.')
  print('Porcentagem de votos nulos: ', porcentagem_nulos)
  print('Porcentagem votos brancos ', votos_brancos)

  if votos_cand1 > votos_cand2 and votos_cand1 > votos_cand3:
   print('O candidato Jair Rodrigues ganhou essa eleição!')
  elif votos_cand2 > votos_cand1 and votos_cand2 > votos_cand3:
   print('O candidato Carlos Luz ganhou essa eleição!')
  elif votos_cand3 > votos_cand2 and votos_cand3 > votos_cand1:
   print('O candidato Neves Rocha ganhou essa eleição!')
  break 
