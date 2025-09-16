#Operações Matematicas

#Menu Inicial:


menu = ("0")
while menu == ("Sair"):
    
    
    if menu == ("Voltar"):
        print("----C E N T R O  D E  C O N T A S  M A T E M Á T I C A S---- \nDigite o numero correspondente da conta matemática! \n 1-Soma \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \n 5-Par ou Impar \n 6-Fatorial \n 7-Primo \n --Digite ''sair'' para sair \n--Digite ''Voltar'' para voltar ao menu")
    
    menu = input()
    
    if menu == ("1"):
        soma1= int(input("Digite o 1º numero a ser somado:"))
        soma2= int(input("Digite o 2º numero a ser somado:"))
        print("A Soma dos numeros são ",soma1+soma2)
        menu = "Sair"
    
menu = input("Voltar")