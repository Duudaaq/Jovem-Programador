print("Quer gerar ou validar um CPF?\n")
print("1 - Gerar")
print("2 - Validar")
print('')
escolha = input('')
print()
if escolha == "1":
    

    import random

    n2= random.randint(1,9)
    n3=random.randint(1,9)
    n4=random.randint(1,9)
    n5=random.randint(1,9)
    n6=random.randint(1,9)
    n7=random.randint(1,9)
    n8=random.randint(1,9)
    n9=random.randint(1,9)
    n10=random.randint(1,9)
    n11 = random.randint(1,10)

    r2 = n2 * 2 
    r3 = n3 * 3
    r4 = n4 * 4
    r5 = n5 * 5
    r6 = n6 * 6
    r7 = n7 * 7
    r8 = n8 * 8
    r9 = n9 * 9
    r10 = n10 * 10
    r11 = n11 * 11

    total1 = (r2+r3+r4+r5+r6+r7+r8+r9+r10)

    t1 = 11 - (total1 % 11)
    if t1 > 9:
        t1 = 0

    total2 = (r2+r3+r4+r5+r6+r7+r8+r9+r10+r11)

    t2 = 11 - (total2 % 11)
    if t2 > 9:
        t2 = 0

    x = (f"{n2}{n3}{n4}.{n5}{n6}{n7}.{n8}{n9}{n10}-{t1}{t2}")
    print(x)

    if len(x) >= 11 or len(x) <= 15:
        print("CPF válido") 
        
    else:
        print('inválido')
        
elif escolha == "2":
    cpf = input("Qual CPF deseja validar?\n")
    if len(cpf) >= 11 or len(cpf) <= 15:
        print("CPF válido") 
        
    else:
        print('inválido')
        
else:
    print()