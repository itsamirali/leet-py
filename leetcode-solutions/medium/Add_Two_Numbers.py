"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# test case

l1 = [2, 4, 3]
l2 = [5, 6, 4]

# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def list_to_int(node, power=0):
            if not node:
                return 0
            return node.val * (10**power) + list_to_int(node.next, power + 1)

        def int_to_list(num):
            if num == 0:
                return ListNode(0)
            node = ListNode(num % 10)
            if num // 10:
                node.next = int_to_list(num // 10)
            return node

        num1 = list_to_int(l1)
        num2 = list_to_int(l2)
        sum_of_l1_l2 = num1 + num2

        return int_to_list(sum_of_l1_l2)


solution = Solution()
print(solution.addTwoNumbers(l1=l1, l2=l2))
