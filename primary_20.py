编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:所有输入只包含小写字母 a-z 。

解题思路：
找公共前缀，肯定需要把最短的那个字符串的长度minlength计算出来，然后比对在0——minlength之间的字符串是否每个字母都相同。。大概思路就是这样，见代码...

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        len_strs=len(strs)
        str_minlen=len(strs[0])
        for i in range(0,len_strs):#算出此数组中最短的那个字符串的长度
            if len(strs[i])<str_minlen:
                str_minlen=len(strs[i])
        answer=""
        for i in range(0,str_minlen):
            target=strs[0][i]#取第一个字符串的第i个字母作为比对的标准
            for j in range(0,len_strs):#对每一个字符串的第i个字母进行比对
                if strs[j][i]!=target:
                    return answer
            answer=answer+target
        return answer

范例代码2：
原理：
os.path.commonprefix(list) 
返回list中，所有path共有的最长的路径。
第一眼你可能还没反应过来，反应过来时已经道出了：妙哉！妙哉！

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        import os
        return os.path.commonprefix(strs)

