n1 = int (input ("Digite um numero \n"))
n2 = int (input ("Digite outro numero \n"))

while True:

    if (n1 > 5 ):
        print("tudo certo, continue")

    elif (n1 < 5) :
        print("erro")

    elif (n2 > 5 ):
        print("erro")

    elif (n2 < 5) :
        print("continue")

    while True:
    
        operação = str (input ("Qual operação sera usada? \n"))

        if (operação == "+"):
            print (n1 + n2)

        elif (operação == "-"):
            print (n1 - n2)

        elif (operação == "*"):
            print (n1 * n2)

        elif (operação == "/"):
            print (n1 / n2)
            continue

        parar = str (input ("Deseja parar o loop?\n"))
        
        if (parar == "s" or "sim"):
                print("stop")
                break

        elif (parar == "n" or "nao"):
                print("continue")
            
    break   