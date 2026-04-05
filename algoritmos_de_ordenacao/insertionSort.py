'''
O Insertion Sort é um algoritmo de ordenação que constrói a parte ordenada do vetor gradualmente. Ele assume que o primeiro elemento já está ordenado e, a partir do segundo, insere cada elemento na posição correta dentro da parte já ordenada. Para isso, desloca os elementos maiores para a direita até encontrar a posição adequada. Esse processo se repete até que todo o vetor esteja ordenado.

- Complexidade
    - Melhor caso: O(n) - ocorre quando o vetor já está ordenado.
    - Caso médio: O(n²) - ocorre devido às inserções em posições intermediárias, exigindo múltiplos deslocamentos de elementos.
    - Pior caso: O(n²) - ocorre quando o vetor está em ordem inversa, exigindo o máximo de deslocamentos a cada inserção.
'''
import random
import time

def insertion_sort(vetor):
    tamanho = len(vetor)

    for i in range(1, tamanho):
        chave = vetor[i]  #Elemento a ser inserido na parte ordenada

        j = i - 1
        while j >= 0 and chave < vetor[j]:
            vetor[j + 1] = vetor[j] #Move o elemento maior uma posição à direita
            j -= 1
        
        vetor[j + 1] = chave #Insere a chave na posição correta. 
    
    return vetor


vetor = [random.randint(0, 10000) for x in range(0, 1000)]

print(f"Before: {vetor}")
start = time.time()
insertion_sort(vetor)
end = time.time()
print(f"After: {vetor}")
print(f"Tempo de execução: {end - start} ")