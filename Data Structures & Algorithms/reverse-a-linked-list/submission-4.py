# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev = None
        while head != None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev = None
        newNode = None
        while curr_node != None:
            newNode = ListNode(curr_node.val, prev)
            prev = newNode
            curr_node = curr_node.next
        return newNode
        