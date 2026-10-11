class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(graph: dict, node: tuple, visited:Optional[set]=None):
            if visited is None:
                visited = set()
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if not neighbor in visited:
                    dfs(graph, neighbor, visited)
        
        
        island_count = 0
        rows = len(grid)
        cols = len(grid[0])

        #construction de graphe
        graph = dict()
        for i in range(rows):
            for j in range(cols):
                graph[(i,j)] = []
                if i-1>=0 and grid[i-1][j] == "1":
                    graph[(i,j)].append((i-1, j))
                if i+1<=rows-1 and grid[i+1][j] == "1":
                    graph[(i,j)].append((i+1, j))
                if j-1>=0 and grid[i][j-1] == "1":
                    graph[(i,j)].append((i, j-1))
                if j+1<=cols-1 and grid[i][j+1] == "1":
                    graph[(i,j)].append((i, j+1))
                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    island_count += 1
                    dfs(graph, (i,j), visited)
        return island_count
                    


                
        

                
        

        