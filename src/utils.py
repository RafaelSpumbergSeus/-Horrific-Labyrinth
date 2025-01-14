#Leitura do arquivo
def load_labyrinth(file_path):
    with open(file_path, 'r') as file:
        lines = file.readLines()
        dimensions = tuple(map(int, lines[0].strip().split()))
        labyrinth = [line.strip().split() for line in lines[1:]]
        return dimensions, labyrinth