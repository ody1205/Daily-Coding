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

class Solution:
    def mergeTwoLists(self, l1, l2):
        l1_cur = l1
        l2_cur = l2
        dummy = ListNode(None)
        cur = dummy
        while l1_cur and l2_cur:
            if l1_cur.val <= l2_cur.val:
                cur.next = l1_cur
                l1_cur = l1_cur.next
            else:
                cur.next = l2_cur
                l2_cur = l2_cur.next
            cur = cur.next
        if l1_cur:
            cur.next = l1_cur
        else:
            cur.next = l2_cur
        return dummy.next


