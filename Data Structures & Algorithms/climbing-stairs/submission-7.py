class Solution:
    def __init__(self) -> None:
        self.dico = {1: 1, 2:2}
    def climbStairs(self, n: int) -> int:
        
        if n == 1 or n == 2:
            return self.dico[n]
        if (n-1) not in self.dico:
            self.dico[n-1] = self.climbStairs(n-1)
        if (n-2) not in self.dico:
            self.dico[n-2] = self.climbStairs(n-2)
        return self.dico[n-1] + self.dico[n-2]

        