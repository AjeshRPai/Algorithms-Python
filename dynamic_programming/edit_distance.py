def minDistance(word1: str, word2: str) -> int:
    dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

    for row in dp:
        print(row)

    for j in range(len(word2) + 1):
        dp[len(word1)][j] = len(word2) - j

    for row in dp:
        print(row)

    for i in range(len(word1) + 1):
        dp[i][len(word2)] = len(word1) - i

    for row in dp:
        print(row)

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                rightNeighbour = dp[i + 1][j]
                bottomNeighbout = dp[i][j + 1]
                rightBottomNeighbour = dp[i + 1][j + 1]
                dp[i][j] = 1 + min(rightNeighbour,bottomNeighbout , rightBottomNeighbour)
    return dp[0][0]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    Output: 2
    print(minDistance(word1,word2))