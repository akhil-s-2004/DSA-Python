#Time Complexity - O(n^2)
#Space Complexity - O(1)
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = list(map(int,input("Enter numbers to sort: ").split()))
print("Unsorted Array: ", arr)
selection_sort(arr)
print("Sorted Array: ", arr)
