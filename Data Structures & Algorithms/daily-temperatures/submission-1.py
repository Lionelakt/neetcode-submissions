class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack[-1]
                res[prev_idx] = idx - prev_idx
                stack.pop()
            stack.append(idx)
        return res
        