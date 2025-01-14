#Converter o labirinto (matriz) em um grafo

def parse_labyrinth(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    directions = {
        0: (-1, 0), #para cima
        1: (0, 1), #direita
        2: (1, 0), #baixo
        3: (0, -1) #esquerda
    }
    
    graph = {}
    for i in range(rows):
        for j in range(cols):
            node = (i, j)
            graph[node] = []
            hex_value = matrix [i][j]
            binary_value = bin(int(hex_value, 16))[2:].zfill(4)
            for bit, (di, dj) in directions.items():
                if binary_value[bit] == '0':
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        graph[node].append((ni, nj))
    
    return graph
                        