#Rather than selecting pivot randomly, select finds as close
#as possible to finding the median then quicksort from there
def kthSmallestMoM(arr, k):
    #Calls select function
    return select(arr, 0, len(arr) - 1, k)

#Divide the array into groups size 5 subarrays and find the median through the medians of the subarrays
def select(arr, left, right, k):
    # If the sublist has less than or equal to 5 elements, find the kth smallest directly
    if right - left < 5:
        arr[left:right + 1] = sorted(arr[left:right + 1])
        return arr[left + k - 1]

    # Divide the list into sublists of size 5 and find the medians
    medians = []
    for i in range(left, right + 1, 5):
        subRight = min(i + 4, right)
        #Gets median from subarrays 
        subMedian = findMedian(arr, i, subRight)
        medians.append(subMedian)

    #Find the median from subarray of medians (Median of Medians)
    pivot = select(medians, 0, len(medians) - 1, len(medians) // 2 + 1)

    # Partition the array using the pivot
    pivotIndex = partitionMoM(arr, left, right,pivot)
    #Adjust for pivot index in subarray
    subPivot = pivotIndex - left + 1

    #Check if k = subPivot
    if k == subPivot:
        return arr[pivotIndex]
    elif k < subPivot:
        return select(arr, left, pivotIndex - 1, k)
    else:
        return select(arr, pivotIndex + 1, right, k - subPivot)

#Takes advantage of the fact sorting is really fast with small inputs
#Sorts small subarray and returns median 
def findMedian(arr, left, right):
    #Sort subarray section of original array
    subarray = arr[left:right + 1]
    subarray.sort()
    medianIndex = (right - left) // 2
    return subarray[medianIndex]

#Similar to partition QS except the value of the pivot is passed and searched for instead of the index
def partitionMoM(arr, left, right,pivot):
    pivotIndex = arr.index(pivot)
    arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]
    pivotValue = arr[right]
    pivotIndex = left

    for i in range(left, right):
        if arr[i] < pivotValue:
            arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i]
            pivotIndex += 1

    arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]
    return pivotIndex


def main():
    # Insert any test array 
    #Test Cases used for Part 1C
    testCase1 = [18, 34, 5, 11, 42]
    testCase2 = [23, 2, 39, 14, 29]
    testCase3 = [43, 19, 5, 31, 9, 38, 14, 26, 47, 12]
    testCase4 = [8, 34, 22, 46, 41, 17, 30, 11, 37, 29]
    testCase5 = [32, 6, 43, 19, 8, 49, 18, 50, 14, 28, 7, 45, 30, 41, 24, 2, 37, 15, 12, 21, 4, 27, 36, 10, 9]
    testCase6 = [22, 29, 1, 35, 16, 26, 5, 38, 48, 39, 33, 3, 40, 47, 17, 34, 20, 23, 31, 13, 42, 44, 11, 25, 46]
    testCase7 = [16, 35, 49, 12, 45, 33, 4, 19, 28, 8, 6, 31, 13, 26, 43, 10, 39, 27, 23, 47, 3, 14, 20, 11, 18, 48, 36, 21, 50, 42, 15, 22, 37, 7, 24, 25, 2, 30, 9, 40, 5, 29, 44, 34, 17, 1, 46, 38, 32, 41]
    testCase8 = [3, 24, 48, 35, 1, 32, 19, 39, 7, 6, 43, 50, 10, 38, 27, 21, 46, 18, 45, 44, 5, 31, 8, 14, 30, 23, 41, 47, 22, 20, 16, 33, 42, 36, 26, 13, 25, 34, 49, 28, 11, 9, 2, 29, 15, 12, 4, 37, 17, 40]
    testCase9 = [8, 25, 44, 1, 48, 29, 45, 47, 29, 38, 6, 36, 26, 47, 43, 19, 2, 48, 4, 50, 39, 44, 49, 1, 28, 3, 46, 50, 37, 11, 26, 45, 46, 48, 19, 33, 33, 27, 14, 10, 9, 18, 25, 17, 19, 13, 7, 16, 35, 35, 39, 14, 23, 25, 29, 29, 29, 49, 15, 28, 20, 47, 1, 10, 34, 3, 2, 18, 36, 44, 33, 43, 48, 9, 19, 22, 13, 38, 18, 29, 31, 5, 2, 47, 15, 45, 47, 31, 28, 11, 30, 3, 7, 44, 20, 28, 17, 25, 16, 18, 31, 21, 7, 20, 46, 18]
    testCase10 = [16, 34, 25, 42, 18, 50, 9, 22, 30, 7, 42, 3, 39, 47, 2, 48, 15, 1, 24, 37, 13, 46, 21, 49, 32, 29, 16, 23, 12, 40, 6, 8, 49, 28, 50, 42, 37, 26, 45, 43, 20, 36, 31, 10, 48, 19, 14, 17, 25, 19, 4, 44, 35, 11, 1, 27, 42, 5, 33, 50, 50, 38, 41, 14, 25, 2, 37, 30, 50, 17, 9, 28, 49, 6, 46, 15, 7, 42, 25, 20, 45, 3, 37, 47, 16, 24, 23, 16, 15, 33, 19, 42, 9, 50, 11, 43, 25, 10, 50, 28, 1, 36, 23, 42, 11, 8, 26]
    k = 26
    result = kthSmallestMoM(testCase7,k)
    print("Array: ")
    print(testCase7)
    print("kth value("+str(k)+") = " + str(result))

main()