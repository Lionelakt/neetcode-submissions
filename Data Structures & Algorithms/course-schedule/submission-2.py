class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        states = {i: "n" for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        def dfs(node):
            states[node] = "c"

            for neighbor in graph[node]:
                if states[neighbor] == "n":
                    if dfs(neighbor):
                        return True
                elif states[neighbor] == "c":
                    return True
            states[node] = "d"
            return False
        
        for course in graph:
            if states[course] == "n":
                if dfs(course):
                    return False
        return True
        








