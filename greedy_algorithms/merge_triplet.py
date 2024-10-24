from typing import List

def mergeTriplets( triplets: List[List[int]], target: List[int]) -> bool:
    target_set = set()
    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue

        for index, value in enumerate(t):
            if value == target[index]:
                target_set.add(index)

    return len(target_set) == 3


# Driver Code with Test Cases
if __name__ == "__main__":
    # Test Case 1
    triplets = [[2, 5, 3], [1, 8, 4], [2, 3, 5]]
    target = [2, 5, 5]
    print(mergeTriplets(triplets, target))  # Output: True

    # Test Case 2
    triplets = [[1, 3, 4], [2, 3, 1], [1, 2, 2]]
    target = [2, 3, 4]
    print(mergeTriplets(triplets, target))  # Output: True

    # Test Case 3
    triplets = [[2, 3, 4], [1, 5, 6], [2, 1, 3]]
    target = [3, 5, 4]
    print(mergeTriplets(triplets, target))  # Output: False

    # Test Case 4
    triplets = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    target = [3, 3, 3]
    print(mergeTriplets(triplets, target))
    # Output: True