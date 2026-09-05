class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for val in strs:
            sorted_key = "".join(sorted(val))
            if sorted_key in dic:
                dic[sorted_key].append(val)
            else:
                dic[sorted_key] = [val]
        return list(dic.values())

