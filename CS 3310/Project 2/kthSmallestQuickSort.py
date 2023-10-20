import random

#Partition array until you find kth value (leaves chunks of the array unsorted)
def kthSmallestQuickSort(arr, k):
    #Set up bounds
    left = 0
    right = len(arr) - 1

    while left <= right:
        #Choose a random pivot 
        pivotIndex = random.randint(left, right)
        #Partition arr using pivot index
        pivotIndex = partition(arr, left, right, pivotIndex)
        
        #Check if pivot = kth index 
        if pivotIndex == k - 1:
            return arr[pivotIndex]
        # If kth smallest element is in left subarray, recurse on left subarray
        elif k - 1 < pivotIndex:
            right = pivotIndex - 1
        # If kth smallest element is in right subarray, recurse on right subarray
        else:
            left = pivotIndex + 1

#Rearranges elements so less = left of pivot, greater = right of pivot
def partition(arr, left, right, pivotIndex):
    # Move the pivot to the end
    pivotValue = arr[pivotIndex]
    # Swap values
    arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]
    pivotPos = left

    # Partition the array
    for i in range(left, right):
        if arr[i] < pivotValue:
            #Swap values so lesser values on left of pivot
            arr[i], arr[pivotPos] = arr[pivotPos], arr[i]
            pivotPos += 1

    # Move the pivot to its final position
    arr[pivotPos], arr[right] = arr[right], arr[pivotPos]

    return pivotPos

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
    k = 18
    result = kthSmallestQuickSort(testCase5,k)
    print("Array: ")
    print(testCase5)
    print("kth value("+str(k)+") = " + str(result))

main()