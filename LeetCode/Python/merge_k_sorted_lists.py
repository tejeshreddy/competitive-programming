"""
Title: 0023 - Merge k Sorted Lists
Tags: Linked List
Time: O(nlogk)
Space: O(1)
Source: https://leetcode.com/problems/merge-k-sorted-lists/
Difficulty: Hard
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def mergeTwoLists(l1, l2):
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

        if not lists:
            return None
        left, right = 0, len(lists) - 1
        while right > 0:
            lists[left] = mergeTwoLists(lists[left], lists[right])
            left += 1
            right -= 1
            if left >= right:
                left = 0
        return lists[0]
