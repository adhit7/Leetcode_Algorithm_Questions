class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        a = ""
        b = abs(x)
        default = 2**31
        while b != 0:
            n1 = b % 10
            a += str(n1)
            b = b//10
        if x < 0:
            a = "-" + a[0:]
        a = int(a)
        if (a > ( default - 1)) or (a < -default):
            return 0
        return a
    