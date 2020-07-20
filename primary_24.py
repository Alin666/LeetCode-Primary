将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
    
        listMerge = None
        if l1.val < l2.val:
            listMerge = l1
            listMerge.next = self.mergeTwoLists(l1.next,l2)
        else:
            listMerge = l2
            listMerge.next = self.mergeTwoLists(l2.next,l1)
        return listMerge


