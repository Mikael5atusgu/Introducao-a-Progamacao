#Misael , Luis f. , Gabriel carezolin
numero = int(input("Digite o numero de queira soma seus primos"))
resto = 0
divisor = 0 
contagem = 0
soma = 0
somatudo = 0

while numero!=0:
    resto = int(numero%10)

    for I in range(1,resto+ 1):
        
        if resto%I == 0:
            contagem += 1

    if contagem == 2:
        soma = resto

    somatudo= somatudo+soma
    soma = 0
    numero= int(numero/10)
    contagem = 0

print("A soma dos numeros primos é:",somatudo)

