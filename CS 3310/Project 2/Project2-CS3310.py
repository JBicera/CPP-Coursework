import random
import time
# --------------------------
#Merge Sort (Algorithm 1)
# --------------------------

#Merge sort the entire array then return kth value
def kthSmallestMergeSort(arr, k):
    #Merge sort list first
    arr = mergeSort(arr)
    #Then return the kth element
    return arr[k - 1]

def mergeSort(arr):
    #Base case when array is size 1
    if len(arr) <= 1:
        return arr
    #Divide in half
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    #Recursively merge sort each half
    left = mergeSort(left)
    right = mergeSort(right)

    #Merge the now sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    #Merge the two halves by comparing elements in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    #Add Remaining elements left in either half
    result += left[i:]
    result += right[j:]

    return result

# --------------------------
# Quicksort (Algorithm 2)
# --------------------------


#Partition array until you find kth value (leaves chunks of the array unsorted)
def kthSmallestQuickSort(arr, k):
    #Set up bounds
    left = 0
    right = len(arr) - 1

    while left <= right:
        #Choose a random pivot 
        pivotIndex = random.randint(left, right)
        #Partition arr using pivot index
        pivotIndex = partitionQS(arr, left, right, pivotIndex)
        
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
def partitionQS(arr, left, right, pivotIndex):
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

# --------------------------
# Median of Medians (Algorithm 3)
# --------------------------

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


# ---------------
# Driver Functions
# ---------------

def alg1Test(arr,k):
    runtimes = []
    m = 15
    for _ in range(m):
        start_time = time.perf_counter()
        kthSmallestMergeSort(arr,k)
        end_time = time.perf_counter()
        result = (end_time - start_time) * 1000 #Convert to milliseconds
        runtimes.append(result)
    total = 0
    for value in runtimes:
        total += value
    average = (total - max(runtimes) - min(runtimes)) / (m-2)
    return average

def alg2Test(arr,k):
    runtimes = []
    m = 15
    for _ in range(m):
        start_time = time.perf_counter()
        kthSmallestQuickSort(arr,k)
        end_time = time.perf_counter()
        result = (end_time - start_time) * 1000
        runtimes.append(result)
    total = 0
    for value in runtimes:
        total += value
    average = (total - max(runtimes) - min(runtimes)) / (m-2)
    return average

def alg3Test(arr,k):
    runtimes = []
    m = 15
    for _ in range(m):
        start_time = time.perf_counter()
        kthSmallestMoM(arr,k)
        end_time = time.perf_counter()
        result = (end_time - start_time) * 1000
        runtimes.append(result)
    total = 0
    for value in runtimes:
        total += value
    average = (total - max(runtimes) - min(runtimes)) / (m-2)
    return average

#Generates random arrays of size n with values from 1-50
def generateRandArrays(n):
    return [random.randint(1, 50) for _ in range(n)]


def main():
    arr2 = generateRandArrays(2)
    arr4 = generateRandArrays(4)
    arr8 = generateRandArrays(8)
    arr16 = generateRandArrays(16)
    arr32 = generateRandArrays(32)
    arr64 = generateRandArrays(64)
    arr128 = generateRandArrays(128)
    arr256 = generateRandArrays(256)
    arr512 = generateRandArrays(512)
    arr1024 = generateRandArrays(1024)
    arr2048 = generateRandArrays(2048)
    arr4096 = generateRandArrays(4096)
    arr8192 = generateRandArrays(8192)
    arr16384 = generateRandArrays(16384)
    arr32768 = generateRandArrays(32768)

    #Algorithm 1 Test
    mergeSortRuntimes = []
    mergeSortRuntimes.append(alg1Test(arr2,len(arr2)//2))
    mergeSortRuntimes.append(alg1Test(arr4,len(arr4)//2))
    mergeSortRuntimes.append(alg1Test(arr8,len(arr8)//2))
    mergeSortRuntimes.append(alg1Test(arr16,len(arr16)//2))
    mergeSortRuntimes.append(alg1Test(arr32,len(arr32)//2))
    mergeSortRuntimes.append(alg1Test(arr64,len(arr64)//2))
    mergeSortRuntimes.append(alg1Test(arr128,len(arr128)//2))
    mergeSortRuntimes.append(alg1Test(arr256,len(arr256)//2))
    mergeSortRuntimes.append(alg1Test(arr512,len(arr512)//2))
    mergeSortRuntimes.append(alg1Test(arr1024,len(arr1024)//2))
    mergeSortRuntimes.append(alg1Test(arr2048,len(arr2048)//2))
    mergeSortRuntimes.append(alg1Test(arr4096,len(arr4096)//2))
    mergeSortRuntimes.append(alg1Test(arr8192,len(arr8192)//2))
    mergeSortRuntimes.append(alg1Test(arr16384,len(arr16384)//2))
    mergeSortRuntimes.append(alg1Test(arr32768,len(arr32768)//2))
    print()
    print("kth Smallest Merge Sort (Algorithm 1) Runtimes:")
    i = 1
    for value in mergeSortRuntimes:
        print("Array size:{} | Runtime: {:.2f}ms".format(2**i,value))
        i+=1

    #Algorithm 2 Test
    quickSortRuntimes = []
    quickSortRuntimes.append(alg2Test(arr2,len(arr2)//2))
    quickSortRuntimes.append(alg2Test(arr4,len(arr4)//2))
    quickSortRuntimes.append(alg2Test(arr8,len(arr8)//2))
    quickSortRuntimes.append(alg2Test(arr16,len(arr16)//2))
    quickSortRuntimes.append(alg2Test(arr32,len(arr32)//2))
    quickSortRuntimes.append(alg2Test(arr64,len(arr64)//2))
    quickSortRuntimes.append(alg2Test(arr128,len(arr128)//2))
    quickSortRuntimes.append(alg2Test(arr256,len(arr256)//2))
    quickSortRuntimes.append(alg2Test(arr512,len(arr512)//2))
    quickSortRuntimes.append(alg2Test(arr1024,len(arr1024)//2))
    quickSortRuntimes.append(alg2Test(arr2048,len(arr2048)//2))
    quickSortRuntimes.append(alg2Test(arr4096,len(arr4096)//2))
    quickSortRuntimes.append(alg2Test(arr8192,len(arr8192)//2))
    quickSortRuntimes.append(alg2Test(arr16384,len(arr16384)//2))
    quickSortRuntimes.append(alg2Test(arr32768,len(arr32768)//2))
    print()
    print("kth Smallest Quick Sort (Algorithm 2) Runtimes:")
    i = 1
    for value in quickSortRuntimes:
        print("Array size:{} | Runtime: {:.2f}ms".format(2**i,value))
        i+=1

    #Algorithm 3 Test
    partitionMoMRuntimes = []
    partitionMoMRuntimes.append(alg3Test(arr2,len(arr2)//2))
    partitionMoMRuntimes.append(alg3Test(arr4,len(arr4)//2))
    partitionMoMRuntimes.append(alg3Test(arr8,len(arr8)//2))
    partitionMoMRuntimes.append(alg3Test(arr16,len(arr16)//2))
    partitionMoMRuntimes.append(alg3Test(arr32,len(arr32)//2))
    partitionMoMRuntimes.append(alg3Test(arr64,len(arr64)//2))
    partitionMoMRuntimes.append(alg3Test(arr128,len(arr128)//2))
    partitionMoMRuntimes.append(alg3Test(arr256,len(arr256)//2))
    partitionMoMRuntimes.append(alg3Test(arr512,len(arr512)//2))
    partitionMoMRuntimes.append(alg3Test(arr1024,len(arr1024)//2))
    partitionMoMRuntimes.append(alg3Test(arr2048,len(arr2048)//2))
    partitionMoMRuntimes.append(alg3Test(arr4096,len(arr4096)//2))
    partitionMoMRuntimes.append(alg3Test(arr8192,len(arr8192)//2))
    partitionMoMRuntimes.append(alg3Test(arr16384,len(arr16384)//2))
    partitionMoMRuntimes.append(alg3Test(arr32768,len(arr32768)//2))
    print()
    print("kth Smallest Median of Medians Quick Sort (Algorithm 3) Runtimes:")
    i = 1
    for value in partitionMoMRuntimes:
        print("Array size:{} | Runtime: {:.2f}ms".format(2**i,value))
        i+=1
main()