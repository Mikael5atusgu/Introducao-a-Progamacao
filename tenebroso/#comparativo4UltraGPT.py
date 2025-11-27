#comparativo4UltraGPT
bateria = int(input("Informe a bateria do Robô: "))
temperatura = float(input("Informe a temperatura do ambiente: "))
umidade = float(input("Informe a umidade do solo: "))
modo = input("Informe o modo do Robô (plantio, colheita ou irrigação) ")

#bateria
if bateria<20:
    print("Bateria muito baixa! Retorne imediatamente para a base.")

if 20<=bateria<50:
    print( "Atenção: bateria em nível moderado.")

if bateria>=50:
    print("Bateria suficiente para operação.")

#temperatura

if temperatura>40:
    print("Temperatura crítica! Operação suspensa")

if temperatura<5:
    print("Frio extremo! Modo de economia ativado.")

#solo

if umidade<30:
    print("Solo muito seco. Recomendado iniciar irrigação.")

if umidade>80:
    print("Solo encharcado! Suspenda irrigação imediatamente.")


#executor------------------

if bateria>=50:

    if 10<temperatura<35:

        if 30<umidade<80:

            print("Robô autorizado a iniciar a operação!")

            #modo-----------------------------------------------

            if modo==("plantio"):
                print("Iniciando modo PLANTIO...")

            if modo==("colheita"):
                print("Iniciando modo COLHEITA...")

            if modo==("irrigação"):
                print("Iniciando modo IRRIGAÇÃO...")
                    
        if 30>umidade>80:
            print("Operação negada! Verifique as condições do ambiente.")
    if 10>temperatura>35:
        print("Operação negada! Verifique as condições do ambiente.")
if bateria<50:
    print("Operação negada! Verifique as condições do ambiente.")
