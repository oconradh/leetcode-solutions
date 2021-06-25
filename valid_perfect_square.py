class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num**(1/2) == int(num**(1/2))
