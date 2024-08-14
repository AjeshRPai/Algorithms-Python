from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1

    while start <= end:
        middle = start + ((end - start) // 2)
        if target > nums[middle]:
            start = middle + 1
        elif target < nums[middle]:
            end = middle - 1
        else:
            return middle

    return start


if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 4))
