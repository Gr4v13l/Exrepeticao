valor_inicial = float(input('Insira o valor que deseja guardar: '))
#rendiemento 5% = 5/100
taxa_rendimento = 0.005
tempo = 12
#por 12 meses, precisa adicionar um numero a mais para ser contabilizado o mes 12
for i in range(1, tempo+1):
    rendimento =  valor_inicial *(1 + taxa_rendimento)**tempo
    print('Seu rendimento foi de :',rendimento)