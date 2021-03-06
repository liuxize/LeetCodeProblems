class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = [0] * 256
        m2 = [0] * 256
        n = len(s)
        for i in range(n):
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            m1[ord(s[i])] = i + 1 #默认值是0 ，所以第0个更新后为1
            m2[ord(t[i])] = i + 1
        return True

if __name__ == "__main__":
    s = Solution()
    res = s.isIsomorphic('aba','cdc')
    print(res)

            