'''
16. 3Sum Closest
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.
Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    def threeSumClosest(self, nums, target):
        res = float('inf')
        nums.sort()
        answer = []
        val = 0
        for i in range(len(nums)-2):
            j = i + 1
            z = len(nums) - 1
            while j < z:
                three = nums[i] + nums[j] + nums[z]
                if three == target:
                    return target
                else:
                    if res > abs(three-target):
                        res = abs(three-target)
                        val = three
                    if three > target:
                        z -= 1
                    else:
                        j += 1
        return val

nums = [1,2,4,8,16,32,64,128]

print(Solution.threeSumClosest(Solution, nums,82))