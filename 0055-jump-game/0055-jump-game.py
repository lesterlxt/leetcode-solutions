class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for idx, step in enumerate(nums[:-1]):
            if farthest >= idx:
                farthest = max(farthest, idx + step)
            else:
                return False

        if farthest >= len(nums) - 1:
            return True
        else:
            return False


        