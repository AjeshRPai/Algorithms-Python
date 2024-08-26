class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) +1)  for i in range(len(s1)+1) ]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), - 1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    return True
                if j<len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    return True
        return dp[0][0]



if __name__ == '__main__':
    solution = Solution()
    solution.isInterleave(s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa")