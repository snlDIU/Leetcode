# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        counterlist = head
        # this part of code count the list length
        while counterlist is not None:
            counter+=1
            counterlist = counterlist.next
        
        # this part of code return the middle node of the linked list
        # // is used to get the flor value of the devision. so 5//2 = 2, 6//2 = 3
        for num in range(counter//2):
            head = head.next
        return head