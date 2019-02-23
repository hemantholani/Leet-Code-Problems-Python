'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        head = ListNode(0)
        current = head
        while l1 or l2:
            if current is None:
                break
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + current.val
            current.val = s%10
            print(current.val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            if s>=10 or l1 or l2:
                current.next = ListNode(s//10)
            else:
                None
            current = current.next
        return head
