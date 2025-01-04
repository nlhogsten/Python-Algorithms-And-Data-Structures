# - - - PROMPT - - -
# REMOVE ELEMENT
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# Space Complexity O(1), one constant
# Time Complexity O(n), iterate through entire list once
print(removeElement([3,2,2,3], 3))
# Output: 2
print(removeElement([0,1,2,2,3,0,4,2], 2))
# Output: 5