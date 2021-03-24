# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。


# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1(object):    #迭代  利用栈实现深度优先 DFS
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []                                              # 定义一个空栈，栈中的元素是结点及其对应的深度
        if root:                                                # 如果根结点不为空
            stack.append((root, 1))                             # 则将根节点及其对应深度1组成的元组入栈
        max_depth = 0                                           # 初始化最大深度为零
        while stack:                                            # 当栈非空时
            tree_node, cur_depth = stack.pop()                  # 弹出栈顶结点及其对应的深度
            if tree_node:                                       # 如果该结点不为空
                max_depth = max(max_depth, cur_depth)           # 更新当前最大深度，如果该结点深度更大的话
                stack.append((tree_node.left, cur_depth+1))     # 将该结点的左孩子结点及其对应深度压入栈中
                stack.append((tree_node.right, cur_depth+1))    # 将该结点的右孩子结点及其对应深度压入栈中
        return max_depth      


class Solution2(object):  # 递归
    def MaxDepth(self,root):
        if not root:
            return 0
        return 1 + max(self.MaxDepth(root.left),self.MaxDepth(root.right))


class Solution3(object):    # 迭代  利用双队列 实现广度优先 BFS
    def MaxDepth(self,root):
        if not root:
            return 0
        queue = deque()    # deque是双端队列，可以从左右两边进行添加，append默认从右边添加，appendleft从左边添加
        queue.append(root)
        res = 0
        while queue:
            res += 1
            for _ in range(len(queue)):
                node = queue.popleft()   # 双端队列可以pop从右边出队列，也可以popleft从左边出队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


# 小结
# DFS深度优先搜索
# 用栈（stack）来实现，整个过程可以想象成一个倒立的树形：
#
# 把根节点压入栈中。
# 每次从栈中弹出一个元素，搜索所有在它下一级的元素，把这些元素压入栈中。并把这个元素记为它下一级元素的前驱。
# 找到所要找的元素时结束程序。
# 如果遍历整个树还没有找到，结束程序。
# BFS广度优先搜索
# 使用队列（queue）来实现，整个过程也可以看做一个倒立的树形：
#
# 把根节点放到队列的末尾。
# 每次从队列的头部取出一个元素，查看这个元素所有的下一级元素，把它们放到队列的末尾。并把这个元素记为它下一级元素的前驱。
# 找到所要找的元素时结束程序。
# 如果遍历整个树还没有找到，结束程序。
# 这次结合之前所做的题，才了解到了这两种基本的策略，有了这两种策略应该大部分树的问题都可以解决了。
# ————————————————
# 版权声明：本文为CSDN博主「RexT1」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_45556599/article/details/104884308
