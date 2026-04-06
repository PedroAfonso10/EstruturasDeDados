'''
O Quick Sort é um algoritmo de ordenação recursivo baseado no princípio de “dividir para conquistar”. Ele escolhe um elemento como pivô (definido na implementação) e particiona o vetor em subconjuntos: elementos menores, iguais e maiores que o pivô. Após a partição, realiza chamadas recursivas para as partes menores e maiores. O processo se repete até que os subvetores tenham tamanho 0 ou 1, resultando no vetor ordenado. 

- Complexidade
    - Melhor caso: O(n log n) - ocorre quando o elemento pivô divide o vetor em duas metades iguais.
    - Caso médio: O(n log n) - ocorre quando o pivô divide em duas partes, mas não necessariamente iguais. 
    - Pior caso: O(n²) - O maior ou menor elemento é o pivô, em cada partição da sublista
'''

import random
import time

def quick_sort(vetor):
    if len(vetor) <= 1: 
        return vetor
    else: 
        pivo = vetor[len(vetor) // 2]
        esquerda = [x for x in vetor if x < pivo]
        meio = [x for x in vetor if x == pivo]
        direita = [x for x in vetor if x > pivo]
        return quick_sort(esquerda) + meio + quick_sort(direita) 
    

vetor = [random.randint(0, 100) for x in range(0, 10)]

print(f"Before: {vetor}")
start = time.time()
vetor = quick_sort(vetor)
end = time.time()
print(f"After: {vetor}")
print(f"Tempo de execução: {end - start} ")