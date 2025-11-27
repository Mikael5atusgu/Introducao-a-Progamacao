totalpreço = 0
quantidadeprodutos = 0
media = 0
maiscaro = 0
compra = 0
preço = 0
while compra!= 1:
    preço = float(input("Preço do produto: "))
    if preço>0:
        totalpreço += preço
        quantidadeprodutos += 1
        media += preço
        if maiscaro<preço:
            maiscaro=preço
        print("Salvo...")
        a = str(input("Quer continuar? (s/n)"))
        if a== "n" :
            compra = 1
    else:
        print("Digite um valor positivo...")

print("----------------------------------\nFicou no total de:",totalpreço,"R$")
print("A quantidade de protudos:",quantidadeprodutos)
print("A media de preço foi",media/quantidadeprodutos)
print("o produto mais caro foi:",maiscaro,"R$")

