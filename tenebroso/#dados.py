#dados
temp = 0
maxtemp = 0
mintemp = 200000
quantidade30 = 0
quantidade15 = 0
media = 0
A = int(input("Quantas leituras de temperatura serão analisadas (um número inteiro N)?"))
for i in range (1,A+1):
    temp = float(input("Digite a temperatura em Cº."))
    
    if temp>maxtemp:
        maxtemp=temp
    if temp<mintemp:
        mintemp=temp
    media += temp

    if temp>30:
        quantidade30 += 1 

    if temp<15:
        quantidade15 += 1 

print("A maior temperatura foi:",maxtemp)
print("A menor temperatura foi:",mintemp)
print("A media de temperatura foi:",(media/A))
print("A quantidade de temperatura acima de 30:",quantidade30)
print("A quantidade de temperatura abaixo de 15:",quantidade15)
if 20<(maxtemp-mintemp):
    print("ALERTA: Variação térmica extrema!")
else:
    print("Variação dentro do esperado.")


    