class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        if num < 1:
            return False
        else:
            return self.isPowerOfFour(num/4)
