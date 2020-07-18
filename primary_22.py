给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_list = []
        while head:
            node_list.append(head)
            if head.next is None:
                break
            else:
                head = head.next

        if len(node_list) == 1:
            return None

        elif len(node_list) == n:
            node_list.pop(0)
            return node_list[0]

        n = 0 - n
        node_list[n - 1].next = node_list[n].next
        node_list.pop(n)
        return node_list[0]
