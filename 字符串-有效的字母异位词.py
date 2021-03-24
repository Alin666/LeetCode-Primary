# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
# 输入: s = "rat", t = "car"
# 输出: false
# 说明:你可以假设字符串只包含小写字母。

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # dic1={}
        # dic2={}
        # for i in s:
        #     if i in dic1:
        #         dic1[i]=dic1[i]+1
        #     else:
        #         dic1[i]=1
        # for i in t:
        #     if i in dic2:
        #         dic2[i]=dic2[i]+1
        #     else:
        #         dic2[i]=1
        # if dic1==dic2:
        #     return true
        # else:
        #     return false
        
        if len(s) != len(t):
            return False
        # print(set(s))  #得到去重的元素
        # print(set(t))
        # print(s.count('a')) #在字符串s中统计a出现的次数
        # print(t.count('a'))
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram('blaack','accklb'))
