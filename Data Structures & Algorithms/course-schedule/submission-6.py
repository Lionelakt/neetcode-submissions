class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Pour traduire, s'il y a des cycles, on returne False
        car on ne peut pas finir puisqu'on se mord la queue"""
        states = {i: "n" for i in range(numCourses)}
        # n -> non visité; c -> en cours; d -> done !
        # on peut faire 0, 1 et 2

        graph = {i: [] for i in range(numCourses)}
        for pair in prerequisites:
            graph[pair[1]].append(pair[0]) 
        #construction de graphe

        def dfs(node):
            #détecte s'il y a un cycle depuis node
            states[node] = "c"
            for neighbor in graph[node]:
                if states[neighbor] == "n":
                    if dfs(neighbor):
                        return True
                elif states[neighbor] == "c":
                    return True
            states[node] = "d"
            return False
        
        #recherche des cycles
        for course in graph:
            if states[course] == "n":
                if dfs(course): #si un cycle détecté
                    return False
        return True #si pas de cycle
        








