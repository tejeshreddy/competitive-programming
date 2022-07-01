"""
Title: 0021 - Merge Two Sorted Lists
Tags: Linked List
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
            
        return dummy.next
