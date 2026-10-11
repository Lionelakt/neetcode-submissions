class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionnary = dict()
        for elt in nums:
            if elt in dictionnary:
                return True
            dictionnary[elt] = None
        return False
                
