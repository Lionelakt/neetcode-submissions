class Solution:
    def isValid(self, s: str) -> bool:

        parenth = dict()
        parenth['['] = ']'
        parenth['('] = ')'
        parenth['{'] = '}'
        stack = []
        i = 0

        for i in range(len(s)):
            if s[i] in parenth: 
                stack.append(s[i])
            elif (stack and parenth[stack[-1]] == s[i]) :
                stack.pop()
            else:
                return False

        return len(stack)==0
                  