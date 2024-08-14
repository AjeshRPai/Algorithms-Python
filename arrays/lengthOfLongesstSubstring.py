from typing import List

from collections import defaultdict


def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        print(charSet)
        while s[r] in charSet:
            print(charSet)
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])

        res = max(res, r - l + 1)
    return res


#Driver code
if __name__ == "__main__":
    s = "zxyzxyz"
    k = lengthOfLongestSubstring(s)
    print(k)
