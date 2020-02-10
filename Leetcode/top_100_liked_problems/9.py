'''
9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

def solution(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

n = 121
print(solution(n))
n1 = -121
print(solution(n1))
n2 = 10
print(solution(n2))
