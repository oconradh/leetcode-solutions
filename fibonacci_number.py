class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            counter = 1
            previous_1 = 1
            previous_2 = 0
            while counter < n:
                fib_n = previous_1 + previous_2
                previous_2 = previous_1
                previous_1 = fib_n
                counter += 1
        return fib_n
