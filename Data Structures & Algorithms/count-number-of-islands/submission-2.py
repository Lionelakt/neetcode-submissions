class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Cas où je ne parcours pas directement
         la grille mais je crée un graphe et je copie-colle
         l'algo dfs que je connais maintenant très bien"""

        #Algorithme de recherche profondeur d'abord
        def dfs(graph: dict, node: tuple, visited:Optional[set]=None):
            if visited is None:
                visited = set()
            visited.add(node)
            for neighbor in graph[node]:
                if not neighbor in visited:
                    dfs(graph, neighbor, visited)
        
        #Données de travail
        island_count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        graph = dict()
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]


        def is_valid(i,j):
            return (0 <= i < rows
            and     0 <= j < cols
            and     grid[i][j] == '1')

        for i in range(rows):
            for j in range(cols):
                graph[(i,j)] = []
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if is_valid(ni,nj) and (ni,nj) not in graph[(i,j)]:
                        graph[(i,j)].append((ni,nj))

        #Boucle de recherche
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    island_count += 1
                    dfs(graph, (i,j), visited)
        return island_count
                    


                
        

                
        

        