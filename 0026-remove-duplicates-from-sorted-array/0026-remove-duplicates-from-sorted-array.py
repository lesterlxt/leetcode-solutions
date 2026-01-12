class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        for read in range(len(nums)):
            if read == 0:
                nums[write] = nums[read]
                write += 1
            if read > 0 and nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
        return write

