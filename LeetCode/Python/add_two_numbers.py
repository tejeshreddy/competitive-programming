"""
Title: 0002 - Add Two Numbers
Tags: LinkedList
Time: O(n)
Space: O(1)
Source: https://leetcode.com/problems/add-two-numbers/
Difficulty: Medium
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode()
        current = temp
        carry = 0
        value = 0
        
        while l1 or l2:
            value = carry
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            carry, value = divmod(value, 10)
            current.next = ListNode(value)
            current = current.next
        
        if carry == 1:
            current.next = ListNode(1)
            
        return temp.next
