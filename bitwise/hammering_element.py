from ctypes import c_ulong


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    # print(solution.hammingWeight(n = c_ulong(0o0000000000000000000000000010111)))