# 统计所有小于非负整数 n 的质数的数量。
# 示例:
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 首先解释一下质数：质数就是只能被1和它本身所整除的数叫质数。

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 双层循环会超时
        # 厄拉多塞 筛法
        if n < 3:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n**0.5) +1):
            if prime[i] == 1:
                prime[i*i:n:i] = [0]*len(prime[i*i:n:i])
        return sum(prime)


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(80))
