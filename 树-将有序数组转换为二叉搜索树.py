# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# 示例:
# 给定有序数组: [-10,-3,0,5,9],
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# 解题思路：因为给定的数组是按照升序排列的，所以可以先取出数组中间位置的值作为二叉查找树的根结点，
# 然后以该数组中间位置的值为中心，将左边的数组划分到根结点的左子树中，右边的数组划分到根结点的右子树中，
# 这样就能保证根结点的左子树上任意结点的值都小于根结点的值，右子树上任意结点的值大于根节点的值。
# 接下来，可以使用递归地方法继续取出左边数组的中间值作为根结点的左子结点，右边数组的中间值作为根结点的右子结点，
# 然后以左边数组中间值为中心，再次划分左右子树，右边数组同理，如此递归下去，对于每个结点，
# 总是能保证其左子树上任意结点的值都要小于该节点的值，其右子树上任意结点的值都要大于该节点的值

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) // 2  # 找到中间节点
        root = TreeNode(nums[mid])  # 当前节点为根节点
        root.left = self.sortedArrayToBST(nums[:mid])  # 小于当前根节点的作为左子树
        root.right = self.sortedArrayToBST(nums[mid + 1:])  # 大于当前根节点的作为右子树
        return root


if __name__ == '__main__':
    s = Solution()
    print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
