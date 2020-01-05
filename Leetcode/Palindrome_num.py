class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = list(str(x))[::-1]
        b = ''.join(a)
        if str(x) == b:
            return True
        else:
            return False