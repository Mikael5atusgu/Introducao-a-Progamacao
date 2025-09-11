altura = float(0)  
Qjogadores = int(input("digite a quantidaoded de jogadores do time!"))
con=0
a=0
while a!=1 :

    altura = altura + float(input("Digite a altura dos jogadores em metros:"))

    if con==Qjogadores :
        a=1
    con+=1

print("a média de altura dos jogadores é:",altura/Qjogadores,"m")