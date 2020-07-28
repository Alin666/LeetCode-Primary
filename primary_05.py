数组：只出现一次的元素

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1
示例 2:
输入: [4,1,2,1,2]
输出: 4

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # length=len(nums)
        # for i in range(0,length,2):
        #     if nums[i]!=nums[i+1]:
        #         return nums[i]
        length = len(nums)
        if length == 1:
            return nums[0]
        myHashMap = {}
        for num in nums:
            myHashMap[num] = myHashMap.get(num, 0) + 1
        for num in nums:
            if myHashMap.get(num) == 1:
                return num

