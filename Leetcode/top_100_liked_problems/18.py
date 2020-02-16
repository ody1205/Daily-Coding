'''
18. 4Sum
Given an array nums of n integers and an integer target, 
are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution:
    def fourSum(self, nums, target):
        s = set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                z = j + 1
                k = len(nums) - 1
                while z < k:
                    four = nums[i] + nums[j] + nums[z] + nums[k]
                    if four == target:
                        tup1 = (nums[i],nums[j],nums[z],nums[k])
                        if tup1 not in s:
                            s.add(tup1)
                        z += 1
                        k -= 1
                    elif four > target:
                        k -= 1
                    elif four < target:
                        z += 1
        return s
print(Solution.fourSum(Solution, [-3,-1,0,2,4,5], 1))

