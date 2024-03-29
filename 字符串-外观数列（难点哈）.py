# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
# 注意：整数序列中的每一项将表示为一个字符串。
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 第一项是数字 1
# 描述前一项，这个数是 1 即 “一个 1 ”，记作 11
# 描述前一项，这个数是 11 即 “两个 1 ” ，记作 21
# 描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211
# 描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221

# 示例 1:
# 输入: 1
# 输出: "1"
# 解释：这是一个基本样例。
# 示例 2:
# 输入: 4
# 输出: "1211"
# 解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        while i <= n:
            if i == 1:
                a = "1"
            else:
                a = self.bb(str(a))
            i += 1
        return a

    def bb(self, n):
        res = []
        count= 0
        for i in range(len(n)):
            if i > 0 and n[i] == n[i - 1]:
                count += 1
                a = str(count) + n[i]
                res[-1] = a
            else:
                count = 1
                a = str(count) + n[i]
                res.append(a)
        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(4))

