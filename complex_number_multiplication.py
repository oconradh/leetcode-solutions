class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a = a.split('+')
        b = b.split('+')
        a_real = a[0]
        b_real = b[0]
        a_complex = a[1].split('i')[0]
        b_complex = b[1].split('i')[0]
        first = int(a_real)*int(b_real)
        outer = int(a_real)*int(b_complex)
        inner = int(a_complex)*(int)(b_real)
        last = int(a_complex)*(int)(b_complex)*-1
        result_real = first+last
        result_complex = outer+inner
        return str(result_real) + '+' + str(result_complex)+'i'
