def partition(nums, low, high):
    i = low - 1  # Index of the smaller element
    pivot = nums[high]  # Pivot element
    
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if nums[j] <= pivot:
            i = i + 1  # Increment the index of the smaller element
            nums[i], nums[j] = nums[j], nums[i]  # Swap elements
            
    # Swap the pivot element with the element at index (i + 1)
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1  # Return the partitioning index

def quickSort(arr, low, high):
    if low < high:
        # Partition the array and get the partitioning index
        pi = partition(arr, low, high)
        
        # Recursively sort elements before and after the partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Test the quickSort function
random = [22, 5, 1, 18, 99]
quickSort(random, 0, len(random) - 1)
print(random)  # Output should be: [1, 5, 18, 22, 99]
