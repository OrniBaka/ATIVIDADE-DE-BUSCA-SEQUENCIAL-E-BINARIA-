def busca_sequencial(lista, alvo):
    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == alvo:
            return comparacoes, i  # Retorna o número de comparações e o índice onde o alvo foi encontrado
    return comparacoes, -1  # Retorna o número de comparações e -1 se o alvo não estiver presente

def busca_binaria(lista, alvo):
    comparacoes = 0
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return comparacoes, meio  # Retorna o número de comparações e o índice onde o alvo foi encontrado
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return comparacoes, -1  # Retorna o número de comparações e -1 se o alvo não estiver presente

# Função para executar os testes e imprimir os resultados
def executar_testes():
    tamanhos_lista = [10, 100, 1000, 10000, 100000]  # Diferentes tamanhos de lista para teste

    for tamanho in tamanhos_lista:
        lista_teste = list(range(1, tamanho + 1))  # Lista ordenada de 1 até tamanho
        alvo_presente = tamanho // 2  # Definindo um alvo que estará presente na lista
        alvo_nao_presente = tamanho + 1  # Definindo um alvo que não estará na lista

        comp_seq_presente, _ = busca_sequencial(lista_teste, alvo_presente)
        comp_bin_presente, _ = busca_binaria(lista_teste, alvo_presente)

        comp_seq_ausente, _ = busca_sequencial(lista_teste, alvo_nao_presente)
        comp_bin_ausente, _ = busca_binaria(lista_teste, alvo_nao_presente)

        print(f"Tamanho da lista: {tamanho}")
        print(f"Busca Sequencial - Alvo presente: {comp_seq_presente} comparações")
        print(f"Busca Binária - Alvo presente: {comp_bin_presente} comparações")
        print(f"Busca Sequencial - Alvo ausente: {comp_seq_ausente} comparações")
        print(f"Busca Binária - Alvo ausente: {comp_bin_ausente} comparações")
        print("------------------------")

# Executando os testes
executar_testes()
