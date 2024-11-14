def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot_index = (low + high) // 2
    pivot = arr[pivot_index]
    # Move pivot to end for easier swapping
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store_index = low

    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    # Move pivot to its final place
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

# Example usage
words = ["apple", "orange", "banana", "grape", "cherry"]
quicksort(words, 0, len(words) - 1)
print("Sorted words:", words)



print("Quicksort Using Auxiliary Arrays Another way to implement quicksort is to use an auxiliary array to hold sorted partitions temporarily rather than sorting the array in place.This method can improve readability and simplify partitioning logic but requires additional memory. The algorithm recursively creates subarrays and combines them by concatenating elements smaller than the pivot, the pivot itself, and elements greater than the pivot. Although this approach is less memory-efficient (with 𝑂(𝑛) O(n) extra space), it can be useful for teaching purposes or in functional programming contexts.")
