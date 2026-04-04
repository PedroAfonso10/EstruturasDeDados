'''
A busca sequencial é um algortimo que percorre elemento por elemento de um vetor, comparando cada valor com o  alvo até encontrar ou até percorrer todo o vetor. 

- Complexidade: 
    - Melhor caso: O(1) - acontece quando o elemento está na primeira posição.
    - Caso médio: O(n) - acontece quando o elemento está distribuído aleatoriamente exigindo em média n/2 comparações.
    - Pior caso: O(n) - acontece quando é necessário percorrer todo o vetor e o elemento está na última posição ou não está localizado no vetor.
'''

def busca_seq(target, vetor):
    tamanho = len(vetor) #Comprimento do vetor
    
    comp = 0 
    for i in range(tamanho): #Percorre todo o vetor em busca do target
        comp += 1
        if target == vetor[i]:
            print(f"Tamanho: {tamanho}")
            print(f"Índice: {i}")
            print(f"Comparações: {comp}")
            return
        
    else:
        print(f"Tamanho: {tamanho}")
        print("Número não localizado")
        print(f"Comparações: {comp}")


#MAIN
vetor1 = [14 ,21 ,5 ,45 ,12 ,3 ,86 ,98 ,46 ,53 ,24 ,2 ,1 ,15 ,90 ,47]
vetor2 = [1 ,2 ,3 ,5 ,12 ,14 ,15 ,21 ,24 ,45 ,46 ,47 ,53 ,86 ,90 ,98]

busca_seq(14, vetor1)
busca_seq(46, vetor1)
busca_seq(90, vetor1)
busca_seq(50, vetor1)

busca_seq(14, vetor2)
busca_seq(46, vetor2)
busca_seq(90, vetor2)
busca_seq(50, vetor2)

'''
Vetor 1:

1° Caso
Tamanho: 16
Índice: 0
Comparações: 1

2° Caso
Tamanho: 16
Índice: 8
Comparações: 9

3° Caso
Tamanho: 16
Índice: 14
Comparações: 15

4° Caso
Tamanho: 16
Número não localizado
Comparações: 16

--------------------------------
Vetor2: 

1° Caso
Tamanho: 16
Índice: 5
Comparações: 6

2° Caso
Tamanho: 16
Índice: 10
Comparações: 11

3° Caso
Tamanho: 16
Índice: 14
Comparações: 15

4° Caso
Tamanho: 16
Número não localizado
Comparações: 16
'''
