'''
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists):
        l, head, pointer = [], None, None
        for i in range(len(lists)):
            head = lists[i]
            while head:
                l.append(head.val)
                head = head.next
                
        l.sort()
        
        while l:
            if head == None:
                head = ListNode(l.pop(0))
                pointer = head
            else:
                pointer.next = ListNode(l.pop(0))
                pointer = pointer.next
        return head


