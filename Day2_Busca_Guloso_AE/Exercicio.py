#Exercício - Busca Gulosa e A*
#Implemente a busca gulosa e a busca A* no mapa da Romênia fornecido
#    Apenas as distâncias de todas as cidades em linha reta até Bucareste são consideradas. Essas distâncias estão na tabela. Ou seja, não se sabe a distância de Arad a Cralova em linha reta, por exemplo, e tudo bem.
#    As distâncias entre os vizinhos são as estradas do mapa, ou seja, as arestas do grafo. As cidades são os nós do grafo.
#    Insira as cidades manualmente no código.
#    A busca gulosa não é a busca cega (que varreria todos os nós), portanto há pelo menos uma função heurística simples, a menor distância do vizinho até Bucareste.
#    A entrada do programa pelo usuário é apenas a cidade da qual desejo partir (origem) para chegar em Bucareste (destino) e o algoritmo de busca escolhido (gulosa ou A*).
#    A saída do programa é o caminho mostrando todas as cidades da origem até Bucareste.
#    Pode ser feito em Java, Python ou C.
#    Enviar o código pelo Moodle para ser analisado.
from traceback import print_tb

cities = {
    'arad': 366,
    'bucharest': 0,
    'craiova': 160,
    'dobreta': 242,
    'eforie': 161,
    'fagaras': 176,
    'giurgiu': 77,
    'hirsova': 151,
    'iasi': 226,
    'lugoj': 244,
    'mehadia': 241,
    'neamt': 234,
    'oradea': 280,
    'pitesti': 100,
    'rimnicu vilcea': 193,
    'sibiu': 253,
    'timisoara': 329,
    'urziceni': 80,
    'vaslui': 199,
    'zerind': 374,
    'cidade nova': 220
}

neighbor = {
    'arad': {
        'sibiu': 140,
        'timisoara': 118,
        'zerind': 75
    },
    'bucharest': {
        'fagaras': 211,
        'giurgiu': 90,
        'pitesti': 101,
        'urziceni': 85,
    },
    'craiova': {
        'dobreta': 120,
        'pitesti': 138,
        'rimnicu vilcea': 146,
    },
    'dobreta': {
        'craiova': 120,
        'mehadia': 75
    },
    'eforie': {
        'hirsova': 85,
    },
    'fagaras': {
        'bucharest': 211,
        'sibiu': 99
    },
    'giurgiu': {
        'bucharest': 90,
    },
    'hirsova': {
        'eforie': 85,
        'urziceni': 98
    },
    'iasi': {
        'neamt': 87,
        'vaslui': 92
    },
    'lugoj': {
        'mehadia': 70,
        'timisoara': 111
    },
    'mehadia': {
        'dobreta': 75,
        'lugoj': 70
    },
    'neamt': {
        'iasi': 87,
        'cidade nova': 85
    },
    'oradea': {
        'zerind': 71,
        'sibiu': 151
    },
    'pitesti': {
        'bucharest': 101,
        'craiova': 138,
        'rimnicu vilcea': 97
    },
    'rimnicu vilcea': {
        'craiova': 146,
        'pitesti': 97,
        'sibiu': 80
    },
    'sibiu': {
        'arad': 140,
        'fagaras': 99,
        'oradea': 151,
        'rimnicu vilcea': 80,
    },
    'timisoara': {
        'arad': 118,
        'lugoj': 111
    },
    'urziceni': {
        'bucharest': 85,
        'hirsova': 90,
        'vaslui': 142
    },
    'vaslui': {
        'iasi': 92,
        'urziceni': 142,
    },
    'zerind': {
        'arad': 75,
        'oradea': 71
    },
    'cidade nova': {
        'neamt': 85
    }
}

def greedySearch(city, path=''):
    if city in cities.keys():
        if city == 'bucharest':
            if path == '':
                return 'Você já está em Bucharest'
            return path

        if path == '':
            print(f'{city} - {cities[city]}')
            path = city
        min = 10000
        newCity = ''

        for n in neighbor[city]:
            if min > cities[n]:
                min = cities[n]
                newCity = n

        print(f'{newCity} - {cities[newCity]}')
        path += " - " + newCity
        return greedySearch(newCity, path)

    return 'Cidade desconhecida'

def AStarSearch(city, visitedCities=[], path=''):
    if city in cities.keys():
        if city == 'bucharest':
            if path == '':
                return 'Você já está em Bucharest'
            return path
        if path == '':
            print(f'{city} - 0 + {cities[city]} = {cities[city]}')
            path = city + "(0)"

        min = 100000
        newCity = ''
        newD = 0

        for n, d in neighbor[city].items():
            dist = 0
            if n in visitedCities:
                dist = cities[n]
            min2 = dist + d + cities[n]
            if min > min2:
                min = min2
                newCity = n
                newD = dist + d

        print(f'{newCity} - {newD} + {cities[newCity]} = {min}')
        path += f" - {newCity} ({newD})"
        visitedCities.append(newCity)
        return AStarSearch(newCity, visitedCities, path)

    return 'Cidade desconhecida'

def menu():
    while True:
        city = ''
        while True:
            city = input('Informe o nome da cidade (ou exit para sair): ')
            if city == 'exit':
                return

            if city not in cities.keys():
                print('Cidade inválida')
            else:
                break

        print('Escolha o tipo de algoritmo')
        print('1 - Busca Guloso')
        print('2 - Busca A*')
        print('0 - exit')

        opt = input('Informe o tipo de busca: ')
        if opt == '1':
            print(greedySearch(city.lower()))
        elif opt == '2':
            print(AStarSearch(city.lower()))
        elif opt == '0':
            break
        else:
            print('Opção inválida')

menu()
