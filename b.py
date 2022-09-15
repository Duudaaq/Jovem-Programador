#Função de fatorial
def fatorial(numero):
    total = 1    
    for i in range(numero):
        if numero-i != 1:
            print(numero - i, end=' * ')
        else:
            print(numero - i, end=' = ')
        total *= (i+1)
    return total   
#Um rei determinou a um sábio que estipulasse uma recompensa por tê-lo vencido em uma partida de xadrez. 
#O sábio, então, respondeu: — Majestade, eu desejo como recompensa a quantidade de grãos de arroz que se 
#obtém adotando-se o seguinte procedimento: percorrendo o tabuleiro de xadrez de cima para baixo e da direita 
#para a esquerda, na primeira casa do tabuleiro, coloque 1 grão de arroz; na segunda casa, 2 grãos de arroz; 
#na terceira, 4 grãos de arroz e assim por diante, de modo que, na n-ésima casa do tabuleiro, devam ser colocados 2n-1 grãos de arroz.
def tabuleiro(casas):
    total = 1
    for i in range(casas-1):
        total *=2
    return total
