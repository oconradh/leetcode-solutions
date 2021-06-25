class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        contained = nums[0:len(nums)-k]
        overflow = nums[len(nums)-k:]
        for i in range(0,k):
            nums[i] = overflow[i]
        for i in range(0, len(contained)):
            nums[i+k] = contained[i]
