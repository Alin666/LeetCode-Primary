# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
# 给定的 n 保证是有效的。
# 进阶：
# 你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1(object):
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


class Solution2(object):
    def removeNthFromEnd(self, head, n):
        next_value = head.val
        head = head.next
        head_list = []
        head_list.append(next_value)
        while 1:
            if not head:
                break
            next_value = head.val
            head_list.append(next_value)
            head = head.next

        L1 = len(head_list)
        if L1 == 1:
            return []
        head_list = head_list[:L1 - n] + head_list[L1 - n + 1:]
        # 建立新的链表l3，用于存储删除节点之后的链表
        l3 = ListNode(head_list[0])
        # 将链表的头结点赋给p1
        p1 = l3
        for i in range(len(head_list) - 1):
            p1.next = ListNode(head_list[i + 1])
            # 向后移动p1指向的位置
            p1 = p1.next
        return l3


class Solution3(object):
    def getKthFromEnd(self, head, k):
        fast = slow = head   # 使用快慢双指针，快指针先执行n+1步，可以实现一次遍历就找到目标节点
        if not head or k <= 0:
            return None
        while k > 0 and fast:
            fast = fast.next
            k -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        return slow   # 这里返回的是被删除的节点
