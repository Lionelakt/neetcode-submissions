class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for chr in s:
            if chr in dict_s:
                dict_s[chr] += 1
            else:
                dict_s[chr] = 0
            
        dict_t = {}
        for chr in t:
            if chr in dict_t:
                dict_t[chr] += 1
            else:
                dict_t[chr] = 0
        return dict_t == dict_s