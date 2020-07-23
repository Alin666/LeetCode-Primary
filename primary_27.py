给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
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







