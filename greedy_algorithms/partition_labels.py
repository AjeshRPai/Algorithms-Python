from typing import List

def partitionLabels(s: str) -> List[int]:
    last_occurence = {}

    for index, letter in enumerate(s):
        last_occurence[letter] = index

    partitions = []
    partition_size = 0
    current_end = 0

    for index, letter in enumerate(s):
        current_end = max(current_end, last_occurence[letter])
        partition_size +=1

        if index == current_end:
            partitions.append(partition_size)
            partition_size = 0

    return partitions


if __name__ == "__main__":
    # Test Case 1
    S = "xyxxyzbzbbisl"
    print(partitionLabels(S))  # Output: [5, 5, 1, 1, 1]

    # Test Case 2
    S = "abcabc"
    print(partitionLabels(S))  # Output: [6]

    # Test Case 3
    S = "eccbbbbdec"
    print(partitionLabels(S))  # Output: [10]

    # Test Case 4
    S = "abacccba"
    print(partitionLabels(S))  # Output: [8]

    # Test Case 5
    S = "aaaaaaa"
    print(partitionLabels(S))  # Output: [7]