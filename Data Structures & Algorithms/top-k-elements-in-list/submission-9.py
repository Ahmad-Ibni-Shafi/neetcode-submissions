class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic= {}
        for i in nums:
            dic[i] = dic.get(i,0)+1
        sort = sorted(dic, key=dic.get, reverse=True)[:k]
        return sort



        # val = dict(sorted(dic.items()))
        # return list(val)[-2:]
