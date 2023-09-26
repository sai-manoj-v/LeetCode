def maxArea(height: [int]) -> int:
    # Initializing area, left pointer and right pointer
    maxArea = 0
    i,j = 0, len(height) - 1

    # Looping over the array from both sides to find max area combination
    while (i < j):

        #Formula for area calculation
        tankArea = min(height[i], height[j]) * (j - i)
        maxArea = max(tankArea, maxArea)

        # Only slide the pointer which has smaller size, there is no point on moving larger height poointer because of the formula for calculating area which is dependent on smaller height pointer.
        if height[i] <= height[j]:
            i += 1
        else: 
            j -= 1
            
    return maxArea

print(maxArea(height = [1,8,6,2,5,4,8,3,7]))
