from typing import List


def removeDuplicates(nums: List[int]) -> int:
    j = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[j - 2]:
            nums[j] = nums[i]
            j += 1
        print("value", nums, "j = ",j)
    return j


# Driver Code
if __name__ == "__main__":
    nums1 = [1, 1, 1, 2, 2, 3]
    k = removeDuplicates(nums1)
    print(nums1)
    print(k)
