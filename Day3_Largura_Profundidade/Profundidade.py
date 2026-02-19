# Implemente a busca em profundidade para o grafo a seguir, seguindo as instruções (site para consulta):
#   Implemente em Java ou Python.
#   Imprima a lista de adjacentes para todos os nós.
#   Permita que o usuário escolha quem é a raiz e qual o nó objetivo.
#   Mostre todo o caminho percorrido a partir da raiz para atingi-lo.

graph = {
    "a": ["b"],
    "b": ["a", "c"],
    "c": ["b", "d", "f"],
    "d": ["c", "g"],
    "e": ["f"],
    "f": ["c", "g", "e"],
    "g": ["d", "h", "f", "i"],
    "h": ["j", "l", "g"],
    "i": ["g", "m", "k"],
    "j": ["l", "h"],
    "k": ["i", "o"],
    "l": ["j", "n", "h"],
    "m": ["p", "i", "q"],
    "n": ["l"],
    "o": ["q", "k", "r"],
    "p": ["m"],
    "q": ["m", "o"],
    "r": ["q"],
}

def profundidade(root, obj, visited=[], msg=""):
    if root == obj:
        return msg

    if len(visited) == 0:
        visited.append(root)
        msg += f"{root} "

    for n in graph[root]:
        if n not in visited and obj not in visited:
            visited.append(n)
            msg += f"-> {n} "
            msg = profundidade(n, obj, visited, msg)

    return msg

def run():
    root, obj = "", ""
    while True:
        root = input("\nInforme o nó raíz: ").lower()
        if root in graph.keys():
            break
        print("Nó desconhecido.")

    while True:
        obj = input("Informe o nó objetivo: ").lower()

        if obj in graph.keys():
            break
        print("Nó desconhecido.\n")

    print(profundidade(root, obj))

if __name__ == "__main__":
    run()