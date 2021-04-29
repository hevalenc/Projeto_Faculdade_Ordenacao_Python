import time

def bubble_sort(b_lista):
    for i in range(len(b_lista)):
        for j in range(len(b_lista) - 1):
            if b_lista[j] > b_lista[j + 1]:
                b_lista[j], b_lista[j + 1] = b_lista[j + 1], b_lista[j]

def insertion_sort(i_lista):
    for index in range(1, len(i_lista)):
        currentValue = i_lista[index]
        currentPosition = index
        while currentPosition > 0 and i_lista[currentPosition - 1] > currentValue:
            i_lista[currentPosition] = i_lista[currentPosition - 1]
            currentPosition = currentPosition - 1
        i_lista[currentPosition] = currentValue

def selection_sort(s_lista):
    for i in range(len(s_lista) - 1):
        min_index = i
        for j in range(i+1, len(s_lista) - 1):
            if s_lista[j] < s_lista[min_index]:
                min_index = j
        s_lista[i], s_lista[min_index] = s_lista[min_index], s_lista[i]


print("*** Insira uma lista com números separados por vírgula ***")
print("----------------------------------------------------------")
entrada = input("Insira a lista: ")
lista_entrada = entrada.split(', ') #conversão da string em uma lista

lista_dados = [] #conversão da lista de strings em uma lista de inteiros
for val in lista_entrada:
    lista_dados.append(int(val))

while True:

    print('\n------------------------------------'
          '\n1 - Ordenar pelo Bubblesort'
          '\n2 - Ordenar pelo Insertionsort'
          '\n3 - Ordenar pelo Selectionsort'
          '\n4 - Comparar os métodos de ordenação'
          '\n5 - Sair\n')
    selecao = int(input('Digite a opção desejada: '))

    if selecao == 1:
        print("\nMÉTODO BUBBLESORT")
        b_lista = lista_dados.copy()
        inicio = time.time()
        bubble_sort(b_lista)
        fim = time.time()
        b_time = fim - inicio
        print("* Tempo de execução do Bubblesort: ", b_time)
        print("* Lista ordenada pelo Bubblesort:\n", b_lista)

    if selecao == 2:
        print("\nMÉTODO INSERTIONSORT")
        i_lista = lista_dados.copy()
        inicio = time.time()
        insertion_sort(i_lista)
        fim = time.time()
        i_time = fim - inicio
        print("* Tempo de execução do Insertionsort: ", i_time)
        print("* Lista ordenada pelo Insertionsort:\n", i_lista)

    if selecao == 3:
        print("\nMÉTODO SELECTIONSORT")
        s_lista = lista_dados.copy()
        inicio = time.time()
        selection_sort(s_lista)
        fim = time.time()
        s_time = fim - inicio
        print("* Tempo de execução do Selectionsort: ", s_time)
        print("* Lista ordenada pelo Selectionsort:\n", s_lista)

    if selecao == 4:
        print("\nCOMPARAÇÃO ENTRE OS MÉTODOS DE ORDENÇÃO")

        b_lista = lista_dados.copy()
        inicio = time.time()
        bubble_sort(b_lista)
        fim = time.time()
        b_time = fim - inicio

        i_lista = lista_dados.copy()
        inicio = time.time()
        insertion_sort(i_lista)
        fim = time.time()
        i_time = fim - inicio

        s_lista = lista_dados.copy()
        inicio = time.time()
        selection_sort(s_lista)
        fim = time.time()
        s_time = fim - inicio

        print("---------------------------------------------------------")
        print("Tempo de execução do Bubblesort:    ", b_time)
        print("Tempo de execução do Insertionsort: ", i_time)
        print("Tempo de execução do Selectionsort: ", s_time)
        print("=========================================================")

        if b_time < i_time and b_time < s_time:
            print("O método de ordenação mais rápido é o Bubblesort")
        elif i_time < b_time and i_time < s_time:
            print("O método de ordenação mais rápido é o Insertionsort")
        else:
            print("O método de ordenação mais rápido é o Selectionsort")

        if b_time > i_time and b_time > s_time:
            print("\nO método de ordenação mais lento é o Bubblesort")
        elif i_time > b_time and i_time > s_time:
            print("\nO método de ordenação mais lento é o Insertionsort")
        else:
            print("\nO método de ordenação mais lento é o Selectionsort")

    elif selecao == 5:
        print('Fim do programa.')
        break
