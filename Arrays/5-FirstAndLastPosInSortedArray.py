class Solution:

    # Implementing binary search to complete in O(log n) time
    def binarySearch(self, nums, target, firstOccurence):

        # Initializing the indexes
        start = 0
        end = len(nums) - 1
        index = -1

        # Looping through the array for target number
        while start <= end:
            mid = (start + end) // 2

            # If number is less than target than update array to include only first half
            if nums[mid] < target:
                start = mid + 1

            # If number is greater than target than update array to include only second half
            elif nums[mid] > target:
                end = mid - 1
            else:

                # If number found
                index = mid

                # If finding first occurence of target
                if firstOccurence:
                    end = mid - 1

                # If finding last occurence of target
                else:
                    start = mid + 1
        return index

    def searchRange(self, nums: [int], target: int) -> [int]:
        return [self.binarySearch(nums, target, True), self.binarySearch(nums, target, False)]
    
    