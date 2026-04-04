'''
A busca binária é um algoritmo que requer um vetor ordenado. A cada chamada recursiva, compara o elemento central do intervalo de busca com o valor alvo e descarta metade do intervalo com base nessa comparação, diminuindo o intervalo de busca até encontrar o elemento ou até que não exista mais um intervalo. 

- Complexidade: 
    - Melhor caso: O(1) - acontece quando o elemento é encontrado na primeira comparação.
    - Caso médio: O(log n) - acontece quando o elemento está distribuído no vetor, exigindo várias reduções no intervalo de busca.
    - Pior caso: O(log n) - acontece quando o elemento não é encontrado ou quando o intervalo de busca é reduzido ao máximo até localizar o elemento.
'''

def busca_bin_recursiva(target, vetor, inicio=0, fim=None, comp=0):
    if fim is None:
        fim = len(vetor) - 1
    
    if inicio > fim: #Condição de parada para impedir novas chamadas recursivas
        print(f"Não Encontrado")
        print(f"Comparações: {comp}")
        return
    
    comp += 1
    meio = (inicio + fim) // 2
    mosca = vetor[meio]

    if mosca == target:
        print(f"Encontrado")
        print(f"Comparações: {comp}")
        return
    elif mosca < target:
        return busca_bin_recursiva(target, vetor, meio + 1, fim, comp) 
    elif mosca > target:
        return busca_bin_recursiva(target, vetor, inicio, meio -1, comp)



#MAIN
vetor1 = [14 ,21 ,5 ,45 ,12 ,3 ,86 ,98 ,46 ,53 ,24 ,2 ,1 ,15 ,90 ,47]
vetor2 = [1 ,2 ,3 ,5 ,12 ,14 ,15 ,21 ,24 ,45 ,46 ,47 ,53 ,86 ,90 ,98]

busca_bin_recursiva(14, vetor1)
busca_bin_recursiva(46, vetor1)
busca_bin_recursiva(90, vetor1)
busca_bin_recursiva(50, vetor1)

busca_bin_recursiva(14, vetor2)
busca_bin_recursiva(46, vetor2)
busca_bin_recursiva(90, vetor2)
busca_bin_recursiva(50, vetor2)

'''
Vetor 1: (Obs: O vetor está desordenado)

1° Caso
Encontrado
Comparações: 4

2° Caso
Não Encontrado
Comparações: 4

3° Caso
Não Encontrado
Comparações: 4

4° Caso
Não Encontrado
Comparações: 4

---------------------------
Vetor 2:

1° Caso
Encontrado
Comparações: 3

2° Caso
Encontrado
Comparações: 4

3° Caso
Encontrado
Comparações: 4

4° Caso
Não Encontrado
Comparações: 4
'''
