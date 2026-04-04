'''
A busca binária é um algoritmo que requer um vetor ordenado. A cada iteração, compara o elemento central do intervalo de busca com o valor alvo e descarta metade do intervalo com base nessa comparação, diminuindo o intervalo de busca até encontrar o elemento ou até que não exista mais um intervalo. 

- Complexidade: 
    - Melhor caso: O(1) - acontece quando o elemento é encontrado na primeira comparação.
    - Caso médio: O(log n) - acontece quando o elemento está distribuído no vetor, exigindo várias reduções no intervalo de busca.
    - Pior caso: O(log n) - acontece quando o elemento não é encontrado ou quando o intervalo de busca é reduzido ao máximo até localizar o elemento.
'''

def busca_bin(target, vetor):
    tamanho = len(vetor) #Comprimento do vetor

    inicio = 0
    fim = tamanho - 1
    comp = 0

    while inicio <= fim:
        comp += 1
        meio = (inicio + fim) // 2 #Índice central do intervalo atual
        mosca = vetor[meio] #Elemento central para a comparação

        if mosca == target:
            print(f"Tamanho: {tamanho}")
            print(f"Índice: {meio}")
            print(f"Comparações: {comp}")
            return
        elif mosca < target: 
            inicio = meio + 1
        elif mosca > target:
            fim = meio - 1

    print(f"Tamanho: {tamanho}")
    print(f"Número não localizado")
    print(f"Comparações: {comp}")
    return


#MAIN
vetor1 = [14 ,21 ,5 ,45 ,12 ,3 ,86 ,98 ,46 ,53 ,24 ,2 ,1 ,15 ,90 ,47]
vetor2 = [1 ,2 ,3 ,5 ,12 ,14 ,15 ,21 ,24 ,45 ,46 ,47 ,53 ,86 ,90 ,98]

busca_bin(14, vetor1)
busca_bin(46, vetor1)
busca_bin(90, vetor1)
busca_bin(50, vetor1)

busca_bin(14, vetor2)
busca_bin(46, vetor2)
busca_bin(90, vetor2)
busca_bin(50, vetor2)

'''
Vetor 1: (Obs: O vetor está desordenado)

1° Caso
Tamanho: 16
Índice: 8
Comparações: 4

2° Caso
Tamanho: 16
Índice: Número não localizado
Comparações: 4

3° Caso
Tamanho: 16
Número não localizado
Comparações: 4

4° Caso
Tamanho: 16
Número não localizado
Comparações: 4

--------------------------------
Vetor2: 

1° Caso
Tamanho: 16
Índice: 5
Comparações: 3

2° Caso
Tamanho: 16
Índice: 10
Comparações: 4

3° Caso
Tamanho: 16
Índice: 14
Comparações: 4

4° Caso
Tamanho: 16
Número não localizado
Comparações: 4
'''