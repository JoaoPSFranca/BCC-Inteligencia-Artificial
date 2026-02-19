# Implemente dois sistemas de busca, um sequencial e outro binário, 
# para realizar buscas de números em um vetor de números crescentes 
# de tamanho 500000 (quinhentos mil). O usuário escolhe o sistema 
# de busca, entra com o número a ser buscado e tem como resposta a 
# posição que o número está (trate se o número não estiver no vetor) 
# e o tempo que levou para encontrar.
import random
import time
from operator import indexOf


def generateVector():
    vet = []
    
    for i in range(500000):
        vet.append(i)
    
    return vet    

def linearSearch(vet, num):
    count = 0
    
    for v in vet:
        if v == num:
            return count - 1
        else: 
            count += 1
    
    return -1

def binarySearch(vet, num, count=0):    
    while len(vet) > 1:
        i = len(vet) // 2

        if num > vet[i]:
            vet = vet[i:]
        elif num < vet[i]:
            vet = vet[:i]
        else:
            return indexOf(vet, num)

    if vet[0] == num:
        return indexOf(vet, num)
    else:
        return -1

def menu():
    print("Modelos de busca: ")
    print("1 - Busca Sequencial")
    print("2 - Busca Binária")
    print("0 - Stop")

    opt = int(input("Escolha uma opcao: "))

    return opt

def start():
    generateVector()

    while True:
        opt = menu()

        if 3 > opt > 0:
            num = int(input("Informe o número a ser pesquisado: "))
            pos, time_search = 0, 0

            if opt == 1:
                start_time = time.time()
                pos = linearSearch(generateVector(), num)
                time_search = time.time() - start_time
            elif opt == 2:
                start_time = time.time()
                pos = binarySearch(generateVector(), num)
                time_search = time.time() - start_time

            if pos != -1:
                print("Número encontrado na posição: ", pos)
                print("tempo: \n", time_search)
        elif opt == 0:
            return
        else:
            print("Opcao invalida!")

start()