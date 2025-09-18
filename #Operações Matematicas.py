#Operações Matematicas

#Menu Inicial:

import os
print("----C E N T R O  D E  C O N T A S  M A T E M Á T I C A S---- \nDigite o numero correspondente da conta matemática! \n 1-Soma \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \n 5-Par ou Impar \n 6-Fatorial \n 7-Primo \n --Digite ''sair'' para sair \n--Digite ''Voltar'' para voltar ao menu")

opcao = input("Digite o opção que queira:")
opcaoM = opcao.upper()

while opcaoM != "SAIR":
    
    #Soma
    if opcao == "1" :
        valorS1 = int(input("Digite o primeiro valor:"))
        valorS2 = int(input("Digite o segundo valor:"))
        print("O valor de",valorS1,"+",valorS2," é ",valorS1+valorS2)
    
    #Subt
    if opcao == "2" :
        valorS1 = int(input("Digite o primeiro valor:"))
        valorS2 = int(input("Digite o segundo valor:"))
        print("O valor de",valorS1,"-",valorS2," é ",valorS1-valorS2)
    
    #Mult
    if opcao == "3" :
        valorS1 = int(input("Digite o primeiro valor:"))
        valorS2 = int(input("Digite o segundo valor:"))
        print("O valor de",valorS1,"x",valorS2," é ",valorS1*valorS2)
    
    #Divi
    if opcao == "4" :
        valorS1 = int(input("Digite o primeiro valor:"))
        valorS2 = int(input("Digite o segundo valor:"))
        print("O valor de",valorS1,"/",valorS2," é ",valorS1/valorS2)
    
    #Par e impar
    if opcao == "5" :
        valorS1 = int(input("Digite o valor:"))
        
        if valorS1%2 == 0:
            print("O valor é PAR")
        
        else:
            print("O valor é IMPAR")        
    
    #Fato
    if opcao == "6" :
        numero = int(input("Digite o numero que queira fatorar!: "))
        fat=1
        contagem = 0
        while contagem != numero :
            
            contagem+=1
            fat *= contagem
        print("o seu numero fatorado é: ",fat)
    
    #Primo
    if opcao == "7" :
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

    
    
    
    
    
    
    input("Aperte ENTER para voltar ao menu")
    os.system("cls")
    print("----C E N T R O  D E  C O N T A S  M A T E M Á T I C A S---- \nDigite o numero correspondente da conta matemática! \n 1-Soma \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \n 5-Par ou Impar \n 6-Fatorial \n 7-Primo \n --Digite ''sair'' para sair \n--Digite ''Voltar'' para voltar ao menu")
    opcao = input("Digite o opção que queira:")
    opcaoM = opcao.upper()
