SValor=0
CValorN=0
for I in  range(20) :
    valor=int(input("digite o valor:"))
    if valor>=0 :
        SValor+=valor
    else :
        CValorN+=1
print("A soma dos valores positibvos é: ",SValor)
print("A quantidade de numeros negativos: ",CValorN)
