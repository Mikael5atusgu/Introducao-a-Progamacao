numero = int(input("Digite o numero para ser se é primo ou não: "))
contagem = 0
if numero<2:
    print("o numero é não é primo")

for I in range(1,numero+ 1):
    
    if numero%I == 0:
        contagem += 1

if contagem == 2:
    print("É numero é primo")
else:
    print("o numero não é primo")


