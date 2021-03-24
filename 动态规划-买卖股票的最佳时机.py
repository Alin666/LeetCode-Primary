# 给定一个数组，它的第i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# 注意：你不能在买入股票前卖出股票。
# 示例 1:
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        这是一道动态规划题：
        递推方程可用下面的方式表示：
        前i天的最大收益 = max(前i-1天的最大收益，第i天的价格-前i-1天中的最小价格)
        dp[i] 表示 如果第i天抛出股票， 所得到的最大收益，那么递推方程可以表示为：
        dp[i] = max(dp[i-1],prices[i] - min(prices[0:i]))
        此时提交的话，会超时，原因在于每使用递推方程一次，就调用一次min(prices[0:i]，
        这将耗费大量的时间，我们可以做这样的调整，每次都用temp保存前i-2天中的最小价格，
        然后每次只需要用temp和prices[i]进行比较即可得到前i-1天中的最小价格，这样就可以通过了
        """
        dp = [0]
        if not bool(prices):
            return 0
        else:
            temp = prices[0]
            for i in range(1,len(prices)):
                temp = min(temp,prices[i])
                dp.append(max(dp[i-1],prices[i] - temp))
            return max(dp)

