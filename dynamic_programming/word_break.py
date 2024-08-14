from typing import List
def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    return dp[0]

if __name__ == '__main__':
    s = "applepenapple"
    wordDict = ["apple", "pen", "ape"]
    print(wordBreak(s,wordDict))
    s = "catsincars"
    wordDict = ["cats", "cat", "sin", "in", "car"]
    print(wordBreak(s,wordDict))