class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days_to_grow = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                day = stack[-1][0]
                temperature = stack[-1][1]
                days_to_grow[stack[-1][0]] = i - day
                stack.pop()          
            stack.append((i, temperatures[i]))
        return days_to_grow

        