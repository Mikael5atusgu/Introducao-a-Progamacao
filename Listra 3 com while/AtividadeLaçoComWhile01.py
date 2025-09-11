a=0
num=0
contag=0
while a!=20 :
    numa = int(input("digite o numero: "))

    if numa>=0 :
        num+= numa
    else :
        contag+=1
    
    a+=1

print("As somas de positivos são ",num,".")
print("São ",contag," numeros negativos.")

    