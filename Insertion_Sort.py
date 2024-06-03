# def insertion_sort(nums):

#     for i in range(1, len(nums)):
#         insert = nums[i]

#         j = i - 1

#         while j >= 0 and nums[j] > insert:
#             nums[j + 1] = nums[j]
#             j -= 1

#         nums[j + 1] = insert


# # Verify if it works
# random = [9, 1, 15, 28, 6]
# insertion_sort(random)
# print(random)






def insertion_sort(nums):
    # Loop over the array starting from the second element
    for i in range(1, len(nums)):
        # Store the current element to be inserted
        insert = nums[i]
        
        # Initialize j to be the index before i
        j = i - 1
        
        # Move elements of the array that are greater than the insert element
        # to one position ahead of their current position
        while j >= 0 and nums[j] > insert:
            nums[j + 1] = nums[j]
            j -= 1
        
        # Insert the element at the correct position
        nums[j + 1] = insert

# Verify if it works
random = [9, 1, 15, 28, 6]
insertion_sort(random)
print(random)  # Output should be: [1, 6, 9, 15, 28]
