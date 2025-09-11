numero = int(input("Digite um número: "))
if numero <= 1:
    print("O número ",numero," não é primo.")
else:
    divisor = 2
    while divisor <= numero // 2:
        if numero % divisor == 0:
            print("O número ",numero," não é primo.")
            break
        divisor += 1
    else:
        print("O número ",numero," é primo.")
