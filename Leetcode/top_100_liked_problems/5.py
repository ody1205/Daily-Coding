'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''
i = '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
i1 = "cbbd"

def solution(s):
    final = ''
    max_length = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > max_length:
                final = s[i:j]
                max_length = len(s[i:j])
    return final

print(solution(i))
print(solution(i1))