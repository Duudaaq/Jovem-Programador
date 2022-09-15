n = str (input ("Qual seu nome? \n"))
i = int (input ("Qual sua idade? \n"))
a = float (input ("Qual sua altura? \n"))
p = float (input ("Qual seu peso? \n"))


imc = int (p / (a ** 2))

print(f"{n} tem {i} anos, seu imc e {imc}")

from datetime import date
data_atual = date.today()
print("0{}/0{}/{}".format (data_atual.day, data_atual.month, data_atual.year))

data_nascimento = (data_atual.year - i)
print(data_nascimento,"Nascimento")

print("imc atual : {:.2f}". format (p / (a * 2)))

print("{} tem {} anos, pesa {}, sua altura e {}, estamos em {}, nasceu em {} e seu imc atual {:.2f}".format  (n,i,p,a,data_atual,data_nascimento, (p/ (a *2))))