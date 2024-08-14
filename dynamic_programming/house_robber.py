from typing import List
def rob(nums: List[int]) -> int:
    dp = [i for i in nums]

    if len(nums)<3 :
        return max(dp[0],dp[1])

    for i in range(2,len(nums)):
        dp[i] = max(
            dp[i-2] + dp[i],
            dp[i-1]
        )
    return dp[len(nums)-1]


if __name__ == '__main__':
    print(rob([1,1,3,3]))
    print(rob(nums=[2,1]))