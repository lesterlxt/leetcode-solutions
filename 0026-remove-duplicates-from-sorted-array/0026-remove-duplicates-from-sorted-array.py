class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for read in range(write, len(nums)):
            if nums[read - 1] != nums[read]:
                nums[write] = nums[read]
                write += 1
        return write
