# - - - PROMPT - - -
# REMOVE DUPLICATE ARRAY ITEMS #01
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

def removeDuplicates(nums):
    k = 1 # First element is always unique
    if not nums:
        return 0 # If list is empty
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]: # Compare array items next to each other
            nums[k] = nums[i]
            k += 1
    return k, nums[:k]

# Space Complexity O(1), one contant k
# Time Complexity O(n), iterate through entire list once
print(removeDuplicates([1,1,2]))
# Output: (2, [1, 2])
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# Output: (5, [0, 1, 2, 3, 4])