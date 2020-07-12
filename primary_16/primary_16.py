给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:
输入: "race a car"
输出: false

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # num=[1,2,3,4,5,6,7,8,9,0]
        # char=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
        # new=[]
        # for i in range(len(s)):
        #     if s[i] in num or s[i] in char:
        #         new.append(s[i])
        # for i in range(len(new)):
        #     if new[i]==new[len(new)-1-i]:
        #         return true
        #     else:
        #         return false
        
        s = re.sub(r'[^A-Za-z\d+]', '', s.lower())
        l = len(s)
        flat = True
        if l == 0:
            return True
        else:
            for i in range(0, l):
                if s[i] == s[l-1-i] and i<l-i-1:
                    flat = flat & True
                elif i >= l-i-1:
                    break
                else:
                    flat = flat & False
            if flat:
 
                return True
            else:
 
                return False

