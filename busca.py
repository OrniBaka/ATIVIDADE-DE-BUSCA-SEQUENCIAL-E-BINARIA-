def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

# Lista de números inteiros ordenados para teste
lista_teste = [2, 4, 7, 10, 13, 18, 22, 27, 31]

# Testando a busca sequencial
print("Busca Sequencial:")
print(busca_sequencial(lista_teste, 13))  # Deve retornar 4 (índice onde está o número 13)
print(busca_sequencial(lista_teste, 20))  # Deve retornar -1 (número 20 não está na lista)

# Testando a busca binária
print("\nBusca Binária:")
print(busca_binaria(lista_teste, 13))  # Deve retornar 4 (índice onde está o número 13)
print(busca_binaria(lista_teste, 20))  # Deve retornar -1 (número 20 não está na lista)
