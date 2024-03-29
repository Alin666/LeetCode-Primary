# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# 进阶：
# 你可以运用递归和迭代两种方法解决这个问题吗？

# 方案1：递归
# 对称的树的左子树和右子树满足以下条件：
# 如果左子树或右子树均为空，则该树对称；
# 如果左子树或右子树只有一个为空，则该树不对称；
# 如果左子树和右子树均不为空，当左子树的左子树和右子树的右子树镜像对称，且左子树的右子树和右子树的左子树镜像对称时，该树对称。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_mirror(p, q):         # 判断左右子树是否镜像对称
            if not p and not q:
                return True
            elif not p and q or p and not q:
                return False
            else:
                return p.val == q.val and is_mirror(p.left, q.right) and is_mirror(p.right, q.left)

        return is_mirror(root, root)


# 方案2：队列
# 对根节点进行非空判断，将根节点的左右子树放在一个队列中；
# 每次成对取出节点，这两个节点其实是二叉树的对称位置，判断这两个节点的相等情况：
# （1）如果两结点均为空，则继续下一轮循环；
# （2）如果两结点只有一个是空，直接返回Fasle；
# （3）如果两结点都不为空，且它们的数值不同，也直接返回False；
# （4）此时两结点的数值一定相等，将它们的左右子结点逆序加入到队列中，保证每一对结点都是对称的位置。
# 如果到最后，队列中为空，则二叉树对称，返回True。


class Solution(object):
    def isSymmetric(self, root):
        """
        队列
        :param root:
        :return:
        """

        if not root:
            return True
        node_queue = [root.left, root.right]    # 在空队列中加入左子树和右子树
        while node_queue:
            left = node_queue.pop(0)            # 依次弹出两个元素
            right = node_queue.pop(0)
            if not right and not left:          # 如果均为空，继续下一个循环
                continue
            if not right or not left:           # 如果只有一个为空，返回False
                return False
            if left.val != right.val:           # 都非空，再判断值是否相等
                return False
            node_queue.append(left.left)        # 将两个左右子树的左右子树逆序加入队列
            node_queue.append(right.right)
            node_queue.append(left.right)
            node_queue.append(right.left)

        return True
