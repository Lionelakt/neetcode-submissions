class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def dict_str(str_i):
            dic = {}
            for chr in str_i:
                if chr in dic:
                    dic[chr] += 1
                else:
                    dic[chr] = 0
            return dic

        results = []
        seen = []
        for i in range(len(strs)):
            if i not in seen:
                results.append([strs[i]])
                seen.append(i)
            for j in range(len(strs)):
                if dict_str(strs[i]).items() == dict_str(strs[j]).items() and j not in seen:
                    results[-1].append(strs[j])
                    seen.append(j)

        return results

