def findMissingNumber(array):
    n = len(array)+1
    n_elements_sum=n*(n+1)//2
    return n_elements_sum-sum(array)

if __name__ == '__main__':
    array = {1, 2, 4, 6, 3, 7, 8}
    missingNumber = findMissingNumber(array)
    print(missingNumber)
