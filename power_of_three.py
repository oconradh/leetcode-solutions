class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        else:
            log = math.log(abs(n),3)
            if math.pow(3, round(log)) == n:
                return True
