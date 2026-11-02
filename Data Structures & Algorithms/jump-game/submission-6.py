class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi = 0
        for i in range(len(nums)):
            if i > maxi:
                return False
            maxi = max(maxi, i + nums[i])
            if maxi >= len(nums) - 1:
                return True

        return True
            




        # def f(i):
        #     if nums[i]==0 and i<len(nums)-1:
        #         return False
        #     if i>=len(nums)-1:
        #         return True
        #     return f(i+nums[i])
            
        # return f(0)