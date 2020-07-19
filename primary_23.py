反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head == None or head.next==None:  # 若链表为空或者仅一个数就直接返回
        # return head 
        # pre = None
        # next = None
        # while(head != None): 
        #     next = head.next     # 1
        #     head.next = pre     # 2
        #     pre = head      # 3
        #     head = next      # 4
        # return pre
        #以下代码为原地反转
        # cur当前节点
        # pre为当前节点的上一个节点，反转后的下一个节点
        # nex为当前节点的下一个节点，反转后的上一个节点
        cur = head
        pre = None
        while cur:
            # 节点原地反转
            nex = cur.next
            cur.next = pre
            pre = cur
            # 进入下一个要反转的节点
            cur = nex
        return pre


