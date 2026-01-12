class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        n = len(nums)
        
        for i in range(n):
            if far >= i:
                far = max(far, nums[i] + i)
            if far >= n - 1:
                return True
        
        return False
