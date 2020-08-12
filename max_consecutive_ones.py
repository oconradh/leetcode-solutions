class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        string = "".join(list(map(str,nums)))
        string = string.split("0")
        maxLength = 0
        for element in string:
            if len(element) > maxLength:
                maxLength = len(element)
        return maxLength
