class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        res[0] = 1
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        
        right_product = 1
        for r in range(n-1,-1,-1):
            res[r] = res[r] * right_product
            right_product = right_product * nums[r]
        return res