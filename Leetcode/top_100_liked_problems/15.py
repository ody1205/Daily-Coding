'''
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        if len(nums) < 3:
            return []
        result_set = set()
        for i in range(n-2):
            j = i+1
            k = n-1
            while j <k:
                
                if nums[i]+nums[j]+nums[k] == 0:
                    tup1 = (nums[i], nums[j], nums[k])
                    if tup1 not in result_set:
                        result_set.add(tup1)
                    j += 1
                    k -= 1
            
                elif nums[i]+nums[j]+nums[k] > 0:
                    k -= 1
                else:
                    j += 1
                    
        return result_set

print(Solution.threeSum(Solution, [-1, 0, 1, 2, -1, -4]))