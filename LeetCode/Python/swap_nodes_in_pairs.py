"""
Title: 0024 - Swap Nodes in Pairs
Tags: Linked List
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/swap-nodes-in-pairs/
Difficulty: Medium
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next and curr.next.next:
            n1, n2, n3 = curr.next, curr.next.next, curr.next.next
            curr.next = n2
            n2.next = n1
            n1.next = n3
            curr = n1
        return dummy.next
        