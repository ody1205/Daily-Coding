class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        a = list(s)
        prev = ''
        num = 0
        for c in a:
            if prev == 'I' and c == 'V':
                num -= 1
                num += 4
            elif prev == 'I' and c == 'X':
                num -= 1
                num += 9
            elif prev == 'X' and c == 'L':
                num -= 10
                num += 40
            elif prev == 'X' and c == 'C':
                num -= 10
                num += 90
            elif prev == 'C' and c == 'D':
                num -= 100
                num += 400
            elif prev == 'C' and c == 'M':
                num -= 100
                num += 900
            else:    
                num += dict[c]
            prev = c
        return num

s = Solution()
a = "IX"

print(s.romanToInt(a))

        