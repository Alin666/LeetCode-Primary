给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
示例：
s = "leetcode"
返回 0
s = "loveleetcode"
返回 2

提示：你可以假定该字符串只包含小写字母。

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s=list(s)
        # dic={}
        # for i in s:
        #     if i in dic:
        #         dic[i]+=1
        #     else:
        #         dic[i]=1
        # for c in sorted(dic, key=dic.get, reverse=True):
        #     if dic[c]==1:
        #         return c
        
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i
        return -1

