class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        for i in range(len(nums)):
            my_set.add(nums[i])
        longest = 0
        for num in my_set:
            if num-1 not in my_set:
                x = num
                count = 0
                while x in my_set:
                    count = count+1
                    x = x+1
                longest = max(longest, count)
        return longest
