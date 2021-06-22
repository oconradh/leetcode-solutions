class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = abs(x)
        x = str(x)
        reversed_x = ""
        for digit in x:
            reversed_x = digit + reversed_x
        reversed_x = int(reversed_x)
        if negative:
            reversed_x = reversed_x * -1
        if reversed_x > (2**31 -1) or reversed_x < (-2**31):
            return 0
        return reversed_x
