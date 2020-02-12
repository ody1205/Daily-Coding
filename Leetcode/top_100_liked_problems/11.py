'''
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Brute Force way kept gave me runtime error. O(n**2)
Had to use two point algorithm. O(pi)
'''
def maxArea(height):
    maxarea = 0
    l = 0
    r = len(height) - 1

    while (l < r):
        maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
        if (height[l] < height[r]):
            l += 1
        else:
            r -= 1

    return maxarea


a = [1,1]
print(maxArea(a))