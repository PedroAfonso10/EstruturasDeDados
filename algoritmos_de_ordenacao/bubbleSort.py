'''
O Bubble Sort é um algoritmo de ordenação que realiza comparações entre elementos adjacentes de um vetor. Ele percorre o vetor comparando pares e trocando os elementos que estão fora de ordem. Assim, a cada passagem, o maior elemento “sobe” até encontrar sua posição ordenada. Esse processo se repete até que o vetor esteja ordenado.

- Complexidade 
    - Melhor caso: O(n) — ocorre quando o vetor já está ordenado e, com a otimização por meio de interrupção usando uma flag de trocas, o algoritmo realiza uma única passagem com apenas comparações.
    - Caso médio: O(n²) — ocorre quando há múltiplas passagens pelo vetor, com várias comparações e trocas entre elementos adjacentes.
    - Pior caso: O(n²) — ocorre quando o vetor está em ordem inversa, exigindo o máximo de comparações e trocas em todas as passagens.
'''
import random
import time

def bubble_sort(vetor):
    tamanho = len(vetor)

    for i in range(tamanho):
        troca = False #Uso da flag para interromper iterações quando o vetor já está ordenado
        for j in range(0, tamanho - i - 1):
            if vetor[j] > vetor[j + 1]: #Troca se o valor for maior que o próximo
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                troca = True

        if not troca:
            break
    
    return vetor


vetor = [random.randint(0, 10000) for x in range(0, 1000)]

print(f"Before: {vetor}")
start = time.time()
bubble_sort(vetor)
end = time.time()
print(f"After: {vetor}")
print(f"Tempo de execução: {end - start} ")
