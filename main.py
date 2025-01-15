import sys
import os

from src.utils import load_labyrinth
from src.parser import parse_labyrinth
from src.algorithms import find_connected_regions, count_entities

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))


#carregar o arquivo do labirinto 

CREATURES = {
    'A': 'Anão',
    'B': 'Bruxa',
    'C': 'Cavaleiro',
    'D': 'Duende',
    'E': 'Elfo',
    'F': 'Feijão'
}

if __name__ == "__main__":
    #nome do arquivo a ser lido 
    file_path = "tests/caso10.txt"
    dimensions, labyrinth = load_labyrinth(file_path)
    
    graph = parse_labyrinth(labyrinth)
    regions = find_connected_regions(graph)
    entity_counts = count_entities(labyrinth, regions)
    
    print("Número de regiões isoladas:", len(regions))
    for i, counts in enumerate(entity_counts):
        translated_counts = {CREATURES.get(k, k): v for k, v in counts.items()}
        most_frequent = max(translated_counts, key=translated_counts.get) if counts else "Nenhum"
        
        print(f"Região {i + 1}: Ser mais frequente: {most_frequent}, Contagem: {translated_counts}")