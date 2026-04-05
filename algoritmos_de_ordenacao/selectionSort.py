'''
O Selection Sort é um algoritmo de ordenação que percorre o vetor buscando, a cada posição, o menor elemento da parte não ordenada. Ao encontrar o menor elemento, realiza uma única troca, colocando-o na posição correta. Esse processo se repete até que o vetor esteja ordenado.

- Complexidade:
    - Em todos os casos: O(n²) - Mesmo com o vetor ordenado, percorre todo o vetor para confirmar o menor elemento.

'''
import random
import time

def selection_sort(vetor): 
    tamanho = len(vetor)

    for i in range(tamanho):
        min_index = i #Índice do menor elemento 

        for j in range(i+1, tamanho): #Percorre a parte não ordenada em busca do menor elemento
            if vetor[j] < vetor[min_index]:
                min_index = j

        vetor[i], vetor[min_index] = vetor[min_index], vetor[i] #Ordena o vetor colocando o menor elemento na posição correta

    return vetor


vetor = [random.randint(0, 10000) for x in range(0, 1000)]

print(f"Before: {vetor}")
start = time.time()
selection_sort(vetor)
end = time.time()
print(f"After: {vetor}")
print(f"Tempo de execução: {end - start} ")