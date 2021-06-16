def printPairs(arr, n, sum):
    # Store counts of all elements
    # in a dictionary
    mydict = dict()

    # Traverse through all the elements
    for i in range(n):

        # Search if a pair can be
        # formed with arr[i]
        temp = sum - arr[i]

        if temp in mydict:
            count = mydict[temp]
            for j in range(count):
                print("(", temp, ", ", arr[i],
                      ")", sep="", end='\n')

        if arr[i] in mydict:
            mydict[arr[i]] += 1
        else:
            mydict[arr[i]] = 1


# Driver code
if __name__ == '__main__':
    arr = [1, 5, 7, -1, 5]
    n = len(arr)
    sum = 6
    printPairs(arr, n, sum)
