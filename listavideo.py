# #Como faz uma lista
# lista_compras = ['banana', 'cenoura', 'laranja']
# print(lista_compras)

# #posição da lista
# print(lista_compras[2])

# #acrescentar novo item
# lista_compras.append('nescau')
# print(lista_compras)

# #inserir novo item numa posicção especifica
# lista_compras.insert(1, 'chocolate')
# print(lista_compras)

# #deletar item pela posição
# del lista_compras[3]
# print(lista_compras)

# #deletar item pelo nome
# lista_compras.remove('nescau')
# print(lista_compras)

# lista_compras.append('V')
# print(lista_compras)

# lista_sonho = []
# #pop serve pra pegar de um lugar, mas se voce só pegar ele serve como delete.
# sonho = lista_compras.pop(-1)
# print(sonho)

# lista_sonho.append(sonho)
# print(lista_compras)
# print(lista_sonho)

# tarefas = []
# #usuario insere uma tarefa e aparece depois na lista de tarefas
# tarefa = input('insira uma tarefa')
# tarefas.append(tarefa)
# print(tarefas)

# #enquanto nao for fazio vai continuar aparecendo
# while tarefa != '':
#     tarefa = input('insira uma tarefa')
#     tarefas.append(tarefa)
# print(tarefas)

lojas = ['rio de janeiro','sao paulo','santa catarina']
faturamento = [10000,20000,30000]

print(lojas)
print(faturamento)

#ordenar listas
faturamento.sort(reverse = True)
print(faturamento)

#tupla organizar
resultados = []

for i in range(3):
    tupla = (lojas[i-1], faturamento[i-1])
    resultados.append(tupla)
print(resultados)