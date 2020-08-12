class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        else:
            return self.addDigits(sum(list(map(int, str(num)))))
