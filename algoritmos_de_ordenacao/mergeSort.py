'''
O Merge Sort é um algoritmo de ordenação recursivo baseado no princípio de “dividir para conquistar”. Ele divide o vetor em subvetores menores até atingir vetores de tamanho 1, que já estão ordenados. Em seguida, durante o retorno das chamadas recursivas, realiza a etapa de merge, combinando esses subvetores de forma ordenada por meio de comparações entre seus elementos. Esse processo continua até que o vetor original esteja completamente ordenado.  

- Complexidade 
    - Em todos os casos: O(n log n) — independentemente da ordem inicial dos dados
'''

import random
import time

def merge_sort(vetor):
    if len(vetor) > 1:
        #Dividir para conquistar
        meio = len(vetor) // 2
        metade_esquerda = vetor[:meio]
        metade_direita = vetor[meio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)
        #"merge" - Combina as duas metades ordenadas
        i = j = k = 0
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] <= metade_direita[j]:
                vetor[k] = metade_esquerda[i]
                i += 1
            else:
                vetor[k] = metade_direita[j]
                j += 1

            k += 1 

        #Adiciona os elementos restantes
        while i < len(metade_esquerda):
            vetor[k] = metade_esquerda[i]
            i += 1
            k += 1
        
        while j < len(metade_direita):
            vetor[k] = metade_direita[j]
            j += 1
            k += 1


vetor = [random.randint(0, 100) for x in range(0, 10)]

print(f"Before: {vetor}")
start = time.time()
merge_sort(vetor)
end = time.time()
print(f"After: {vetor}")
print(f"Tempo de execução: {end - start} ")