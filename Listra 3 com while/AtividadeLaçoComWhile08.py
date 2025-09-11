numero = int(input("Digite o numero que queira fatorar!: "))
fat=1
contagem = 0
while contagem != numero :
    
    contagem+=1
    fat *= contagem

print("o seu numero fatorado é: ",fat)