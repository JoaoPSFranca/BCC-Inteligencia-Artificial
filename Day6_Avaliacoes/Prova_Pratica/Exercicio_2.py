graph = {
    1: [15, 14],
    2: [15, 17],
    3: [17, 18, 4],
    4: [3, 5],
    5: [4, 6, 9],
    6: [5, 7],
    7: [6, 19],
    9: [5, 10],
    10: [9, 13],
    12: [14],
    13: [14, 10],
    14: [1, 12, 13, 16],
    15: [1, 2],
    16: [14],
    17: [2, 3],
    18: [3],
    19: [7]
}

def wideSearch(root, obj, sons=[], visited=[], msg=""):
    if obj == root:
        return msg

    if len(visited) == 0:
        visited.append(root)
        msg += f"{root} "

    for n in graph[root]:
        if n not in visited:
            if n != obj:
                sons.insert(0, n)
                visited.append(n)
                msg += f"-> {n} "
            else:
                msg += f"-> {n} "
                return msg

    root = sons.pop()
    msg = wideSearch(root, obj, sons, visited, msg)
    return msg

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
    root, obj = 3, 13

    print("Busca em Largura: \n" + wideSearch(root, obj))
    print("Busca em Profundidade: \n" + profundidade(root, obj))

if __name__ == "__main__":
    run()