#identifica as regiões no grafo
def find_connected_regions(graph):
    visited = set()
    regions = []
    
    def dfs(node, region):
        visited.add(node)
        region.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, region)
    
    for node in graph:
        if node not in visited:
            region = []
            dfs(node, region)
            regions.append(region)
            
    return regions

# contatador das entidades
def count_entities(matrix, regions):
    entity_count_per_region = []
    for region in regions:
        entity_count = {}
        for cell in region:
            i, j = cell
            entity = matrix[i][j]
            if entity.isalpha():
                entity_count[entity] = entity_count.get(entity, 0) + 1
        entity_count_per_region.append(entity_count)
    return entity_count_per_region