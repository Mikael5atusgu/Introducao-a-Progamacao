ha = 1.10
th = 1.50
A = 100
contagem = 0
for anos in range(A) :
    ha += 0.03
    th += 0.02
    contagem += 1

    if ha>th :
        print("O Homem-Aranha será mais alto do que o Thanos depois de:",contagem,"anos")

        break
