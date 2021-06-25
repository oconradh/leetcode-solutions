class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if 0 != nums[0]:
            return 0
        for index in range(0, len(nums) - 1):
            if nums[index] + 1 != nums[index + 1]:
                return nums[index] + 1
        return nums[len(nums) - 1] + 1
