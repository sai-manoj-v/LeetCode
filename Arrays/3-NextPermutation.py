def nextPermutation(self, nums: [int]) -> None:

    # Determine which element in the list is to be swapped for the next permutation
    swapIndex = -1
    numsLen = len(nums)

    # Loop through list and find which element has the next element greater than itself 
    for i in range(numsLen - 2, -1, -1):
        if (nums[i] < nums[i+1]):
            swapIndex = i
            break

    # If there is no such element, reverse the list and return - this means there is no next permutation
    if swapIndex == -1:
        nums.reverse()
        print(nums)
        return nums

    lgIndex = -1
    lgValue = 101

    # Find least greater value after the swap element in the list - This is the element that replaces swap element for next permutation
    for i in range(numsLen - 1, swapIndex, -1):
        if (nums[i] > nums[swapIndex]) and (nums[i] < lgValue):
            lgIndex = i
            lgValue = nums[i]

    # Swap least greater value and swap element
    swapElements = nums[swapIndex], nums[lgIndex]
    nums[lgIndex], nums[swapIndex] = swapElements

    # Reverse the list after swap index so that it follows ascending order
    nums[swapIndex+1:] = nums[swapIndex+1:][::-1]
    
    return nums
