'''
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def solution(s):
    n = len(s)
    ans = 0
    a = {}
    i = 0
    for j in range(n):
        if s[j] in a: 
            i = max(a[s[j]], i)
        ans = max(ans, j - i + 1)
        a[s[j]] = j + 1
    return ans

s = "pwwkew"
print(solution(s))