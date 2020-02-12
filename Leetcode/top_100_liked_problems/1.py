'''
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

brute-force O(n**2)
one-hash O(n)
'''
def solution(n,t):
    seen = {}
    for i, j in enumerate(n):
        r = t - j
        if r in seen:
            return [seen[r], i]
        seen[j] = i
    return []


n = [2,7,11,15]
y = 9
print(solution(n,y))