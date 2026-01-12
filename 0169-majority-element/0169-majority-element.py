class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                candidate = nums[i]
                cnt = 1
            else:
                if nums[i] == candidate:
                    cnt += 1
                else:
                    cnt -= 1
        return candidate


