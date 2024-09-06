from typing import List

def singleNumber(nums: List[int]) -> int:
    res = 0
    for n in nums:
        res = n ^ res
    return res

if __name__ == '__main__':
    print(singleNumber(nums= [1,1,2,3,3]))