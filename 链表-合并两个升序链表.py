# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1(object):   # 递归调用
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


class Solution2(object):   # 构建列表
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 and not pHead2:
            return
        res = []
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                res.append(pHead1)
                pHead1 = pHead1.next
            else:
                res.append(pHead2)
                pHead2 = pHead2.next
        while pHead1:
            res.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            res.append(pHead2)
            pHead2 = pHead2.next
        n = len(res)
        for i in range(n):
            if i == n - 1:
                res[i].next = None
            else:
                res[i].next = res[i + 1]
        return res[0]


class Solution3(object):   # 构建两个头节点
    def Merge(self, pHead1, pHead2):
        # write code here

        res = head = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                head.next = pHead1
                pHead1 = pHead1.next
            else:
                head.next = pHead2
                pHead2 = pHead2.next
            head = head.next
        if pHead1:
            head.next = pHead1
        if pHead2:
            head.next = pHead2
        return res.next