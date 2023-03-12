prime = int(input("Entre com o primeiro número: "))
ult = int(input("Entre com o último número: "))

if ult < prime:
    for i in range(prime, ult-1, -1):
        print(i)
else:
    for i in range(prime, ult+1):
        print(i)