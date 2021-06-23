class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for element in nums:
            if element != 0:
                nums[counter] = element
                counter += 1
        while counter < len(nums):
            nums[counter] = 0
            counter += 1
