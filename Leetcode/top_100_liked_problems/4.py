'''
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''
class Solution:
    def findMedianSortedArrays(nums1, nums2):
        nums = nums1 + nums2
        
        nums.sort()
        print(nums)
        if len(nums)%2 == 0:
            return (nums[(len(nums)//2)-1]+nums[len(nums)//2])/2
        else:
            return nums[len(nums)//2]

print(Solution.findMedianSortedArrays([1, 2], [3, 4]))
        