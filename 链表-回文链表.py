# 请判断一个链表是否为回文链表。
#
# 示例 1:
# 输入: 1->2
# 输出: false
# 示例 2:
# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1(object):    # 将链表中的值用list存放，然后判断list是否符合回文的要求
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        l = []
        p = head
        while p.next:
            l.append(p.val)
            p = p.next
        l.append(p.val)
        return l == l[::-1]


class Solution2(object):  # 设置快慢指针，翻转前半部分的链表，然后和后半部的链表进行对比。
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        prev = None
        fast = slow = head
        while fast and fast.next:  # 翻转链表的前n/2个结点，prev为翻转后的头结点
            fast = fast.next.next
            prev, prev.next, slow = slow, prev, slow.next
        if fast:  # 结点个数为奇数时，跳过最中间的结点
            slow = slow.next
        while slow and slow.val == prev.val:  # 前n/2个结点翻转后，与剩下的结点进行对比
            prev, slow = prev.next, slow.next
        return not prev

