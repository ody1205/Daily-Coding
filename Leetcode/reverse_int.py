class Solution:
    def reverse(self, x: int) -> int:
        a = list(str(x))[::-1]
        neg = False
        if a[-1] == '-':
            a.remove('-')
            neg = True
        result = ''.join(a)
        b = int(result)
        if neg == True:
            b = -b
        if -(2**31) <= b <= 2**31-1:
            return b
        else:
            return 0

s = Solution()
x = -12300
print(s.reverse(x))