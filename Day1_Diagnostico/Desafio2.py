# Implemente 3 métodos de ordenação de vetores (BubbleSort, SelectionSort e QuickSort)
# para ordenar um vetor com números aleatórios e não repetidos de tamanho 100000
# (cem mil). O usuário escolhe o metodo de ordenação e tem como resposta o tempo de
# execução e a impressão na tela das posições 0, 10000, 20000, 30000, 40000, 50000,
# 60000, 70000, 80000, 90000 e 99999 do vetor. Deixe o vetor aleatório novamente antes
# de voltar ao menu.
import random
import time

def generateVector():
    arr = [x for x in random.sample(range(0, 100000),100000)]

    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+i], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def partition(lista, inicio, fim):
    pivo = lista[inicio]
    anterior = inicio + 1
    posterior = fim

    while True:
        while anterior <= posterior and lista[anterior] <= pivo:
                anterior += 1
        while anterior <= posterior and lista[posterior] > pivo:
            posterior -= 1

        if anterior <= posterior:
            lista[anterior], lista[posterior] = lista[posterior], lista[anterior]
        else:
            lista[inicio], lista[posterior] = lista[posterior], lista[inicio]
            return posterior

def quick_sort(arr, fim=None, inicio=0):
    if fim is None:
        fim = len(arr) - 1

    if inicio < fim:
        pivo = partition(arr, inicio, fim)
        quick_sort(arr, inicio, pivo - 1)
        quick_sort(arr, pivo + 1, fim)

    return arr

def menu():
    print("Modelos de ordenação: ")
    print("1 - Bubble Sort")
    print("2 - Selection Sort")
    print("3 - Quick Sort")
    print("0 - Stop")

    opt = int(input("Escolha uma opcao: "))

    return opt

def start():
    arr = generateVector()

    while True:
        opt = menu()

        if 4 > opt > 0:
            if opt == 1:
                start_time = time.time()
                arr2 = bubble_sort(arr[:])
                time_order = time.time() - start_time