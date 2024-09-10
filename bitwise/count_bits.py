from typing import List

def countBits(n: int) -> List[int]:
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp

if __name__ == '__main__':
    countBits(00000000000000000000000000010101)

# Input: n = 00000000000000000000000000010101
# Output:    2818572288 (10101000000000000000000000000000)