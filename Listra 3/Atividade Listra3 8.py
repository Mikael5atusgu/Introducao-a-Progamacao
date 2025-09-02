numero = int(input("Digite o numero que queira fatorar!: "))
fat=1
for I in range(1,numero+1):
    fat *= I 

print("o seu numero fatorado é: ",fat)