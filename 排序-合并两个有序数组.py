# 给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
# 说明:
#
# 初始化nums1 和 nums2 的元素数量分别为m 和 n 。
# 你可以假设nums1有足够的空间（空间大小大于或等于m + n）来保存 nums2 中的元素。
#
# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出:[1,2,2,3,5,6]

class Solution(object):

        def merge_sort(self, nums1, nums2):
            m = []
            i, j = 0, 0
            l_1, l_2 = len(nums1)-1, len(nums2)-1
            # 当i，j的索引位置小于等于索引最大值的时候
            while i <= l_1 and j <= l_2:
                if nums1[i] <= nums2[j]:
                    m.append(nums1[i])
                    i += 1
                else:
                    m.append(nums2[j])
                    j += 1
            m = m + nums1[i:] + nums2[j:]
            return m


if __name__ == '__main__':
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 4, 5, 6, 7]
    s = Solution()
    m = s.merge_sort(n1, n2)
    print(m)
    # [1, 2, 2, 3, 4, 4, 5, 5, 6, 7]
