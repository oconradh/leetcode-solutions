class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums2 = []
        for element in nums:
            if (element in nums2):
                nums2.remove(element)
            else:
                nums2.append(element)
        return nums2.pop()
