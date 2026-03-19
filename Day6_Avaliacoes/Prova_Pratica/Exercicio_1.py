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
    'prova city': 280,
    'rimnicu vilcea': 193,
    'sibiu': 253,
    'timisoara': 329,
    'urziceni': 80,
    'vaslui': 199,
    'zerind': 374
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
        'mehadia': 75,
        'prova city': 100
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
        'lugoj': 70,
        'prova city': 110
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
    'prova city': {
        'mehadia': 110,
        'dobreta': 100
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

def greedySearch(city, path='', visitedCities=None):
    if visitedCities is None: visitedCities = []
    if city not in cities.keys():
        return 'Cidade desconhecida'

    if city == 'bucharest':
        if path == '':
            return 'Você já está em Bucharest'
        return path

    visitedCities.append(city)  # Marca a Cidade como Visitada

    if path == '':
        print(f'\n{city} - {cities[city]}')
        path = '\n' + city
    min = 10000
    newCity = ''

    for n in neighbor[city]:
        if min > cities[n] and cities[n] not in visitedCities:
            min = cities[n]
            newCity = n

    if newCity == '':
        return 'Caminho impossível'

    print(f'{newCity} - {cities[newCity]}')
    path += " - " + newCity
    return greedySearch(newCity, path)

def AStarSearch(city, totalDist=0, visitedCities=None, path=''):
    if visitedCities is None: visitedCities = []
    if city not in cities: return 'Cidade desconhecida'

    if city == 'bucharest':
        return path if path != '' else 'Você já está em Bucharest'
    if path == '':
        print(f'\n{city} - 0 + {cities[city]} = {cities[city]}')
        path = '\n' + city + "(0)"

    visitedCities.append(city)  # Marca a cidade como visitada

    min_val = 100000
    newCity = ''
    newD = 0

    for n in neighbor[city]:
        if n not in visitedCities:
            d = totalDist + neighbor[city][n]  # g(n)
            f = d + cities[n]  # f(n) = g(n) + h(n)
            if min_val > f:
                min_val = f
                newCity = n
                newD = d

    if newCity == '':
        return 'Caminho impossível'

    print(f'{newCity} - {newD} + {cities[newCity]} = {min_val}')
    path += f" - {newCity} ({newD})"
    return AStarSearch(newCity, newD, visitedCities, path)

def menu():
    while True:
        city = 'prova city'

        print('Escolha o tipo de algoritmo')
        print('1 - Busca Guloso')
        print('2 - Busca A*')
        print('0 - exit')

        opt = input('Informe o tipo de busca: ')
        if opt == '1':
            print(greedySearch(city.lower()) + '\n')
        elif opt == '2':
            print(AStarSearch(city.lower()) + '\n')
        elif opt == '0':
            break
        else:
            print('Opção inválida')

menu()
