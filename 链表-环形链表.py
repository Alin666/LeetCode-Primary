# 给定一个链表，判断链表中是否有环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

# 示例 1：
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。

# 示例 2：
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。

# 示例 3：
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。

# 进阶：
# 你能用 O(1)（即，常量）内存解决此问题吗？

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         s = set()
#         cur = head
#         while cur:
#             if cur in s:
#                 return cur
#             s.add(cur)
#             cur = cur.next
#         return None


class Solution2(object):  # 使用快慢指针
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        可以考虑用两个指针，slow和fast，当这两个指针重叠之后，则表示这个链表有环
        """
        if not head or not head.next:
            return False

        slow, fast = head, head

        while slow and fast:  # 如果跳出这个循环，说明链表有尽头，无环
            try:  # 用来规避fast.next 就是none这个情况
                slow = slow.next
                fast = fast.next.next

                if slow is fast:  # 这一步是关键，可以通过is来判断节点是不是在同一个内存地址里（也就是是否是同一个）
                    return True
            except:
                return False
        return False


class Solution3(object):  # 更简易的写法
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
            else:
                return False
