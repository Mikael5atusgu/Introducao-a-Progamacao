altura = float(0)  
Qjogadores = int(input("digite a quantidaoded de jogadores do time!"))
for I in range(Qjogadores) :

    altura = altura + float(input("Digite a altura dos jogadores em metros:"))

print("a média de altura dos jogadores é:",altura/Qjogadores,"m")