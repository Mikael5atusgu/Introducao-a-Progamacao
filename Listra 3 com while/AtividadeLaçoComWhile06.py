Caprovado = 0 
Creprovados = 0
Mmaior = 0
Mmenor = 99
contagem=0
while contagem != 10:
    
    contagem+=1
    nota1 = float(input("Digite a nota 1 :"))
    nota2 = float(input("Digite a nota 2 :"))
    nota3 = float(input("Digite a nota 3 :"))

    medianota = ((nota1+nota2+nota3)/3)

    
    if medianota>=6:
        print("Este aluno está APROVADO!")
        Caprovado = Caprovado + 1

    else:
        print("Este aluno está REPROVADO!")
        Creprovados = Creprovados + 1
    
    if medianota > Mmaior :
        Mmaior= medianota

    if medianota < Mmenor :
        Mmenor= medianota
    
print("A menor média é ",Mmenor,)
print("A maior média é ",Mmaior,)
print("São ",Caprovado," alunos Aprovados")

print("São ",Creprovados," alunos Reprovados")