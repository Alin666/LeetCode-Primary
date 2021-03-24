# 数组：两个数组的交集II

# 给定两个数组，编写一个函数来计算它们的交集。

# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
# 示例 2:
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]

# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
# 进阶:
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # res=[]
        # for i in nums1:
        #     if i in nums2:
        #         res.append(i)
        # return res
        if nums1 and not nums2:
            return []
        if not nums1 and nums2:
            return []
        if not nums1 and not nums2:
            return []
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        myHashMap = {}
        result = []
        for index1 in nums1:
            if index1 not in myHashMap:
                myHashMap[index1] = 1
            else:
                myHashMap[index1] += 1
        for index2 in nums2:
            if index2 in myHashMap and myHashMap[index2] > 0:
                result.append(index2)
                myHashMap[index2] -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.intersect([4,9,5], [9,4,9,8,4]))