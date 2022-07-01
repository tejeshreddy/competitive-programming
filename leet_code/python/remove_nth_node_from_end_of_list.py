"""
Title: 0019 - Remove Nth Node From End of List
Tags: Linked List
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Difficulty: Medium
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        
        for i in range(n):
            fast = fast.next
        
        while fast.next:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next
        
        return dummy.next
