Caprovado = 0 
Creprovados = 0
Mmaior = 0
Mmenor = 99
for I in range(10):
    nota1 = float(input("Digite a nota 1 :"))
    nota2 = float(input("Digite a nota 2 :"))
    nota3 = float(input("Digite a nota 3 :"))

    medianota = ((nota1+nota2+nota3)/3)

    print("a média do aluno ",I+1," é ",medianota,)
    
    if medianota>=6:
        print("O aluno",I+1," está APROVADO!")
        Caprovado = Caprovado + 1

    else:
        print("O aluno",I+1," está REPROVADO!")
        Creprovados = Creprovados + 1
    
    if medianota > Mmaior :
        Mmaior= medianota

    if medianota < Mmenor :
        Mmenor= medianota
    
print("A menor média é ",Mmenor,)
print("A maior média é ",Mmaior,)
print("São ",Caprovado," alunos Aprovados")

print("São ",Creprovados," alunos Reprovados")
