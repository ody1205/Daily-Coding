'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
def solution(n):
    if (-2)**31 < n < (2**31) - 1:
        if n < 0:
            n = list(str(n))
            num = -int(''.join(n[1:len(n)+1][::-1]))
            if num >= (-2)**31:
                return num
            else:
                return 0
                
        else:
            n = list(str(n))
            num = int(''.join(n[::-1]))
            if num <= (2**31) - 1:
                return num 
            else:
                return 0
    else:
        return 0

print(solution(1534236469))