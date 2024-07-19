from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if n == 0: return
    len1 = len(nums1)
    end_idx = len1 - 1
    while n > 0 and m > 0:
        if nums2[n - 1] >= nums1[m - 1]:
            nums1[end_idx] = nums2[n - 1]
            n -= 1
        else:
            nums1[end_idx] = nums1[m - 1]
            m -= 1
        end_idx -= 1
    while n > 0:
        nums1[end_idx] = nums2[n - 1]
        n -= 1
        end_idx -= 1


# Driver Code
if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
