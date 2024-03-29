# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        levels = []

        def backtrack(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)

            if node.left:
                backtrack(node.left, level + 1)
            if node.right:
                backtrack(node.right, level + 1)

        backtrack(root, 0)
        return levels


class Solution2(object):
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        cur_nodes = []
        next_nodes = []
        res.append(i.val for i in cur_nodes)
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next.nodes.append(node.right)
            if next_nodes:
                res.append([i.val for i in next_nodes])
            cur_nodes = next_nodes
            next_nodes = []
        return res