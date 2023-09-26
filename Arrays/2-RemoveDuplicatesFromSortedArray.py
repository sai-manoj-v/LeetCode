class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        # Pointer that only shifts with unique values
        turtle = 1

        # Loop through array for unique values (Hare runs faster for every value)
        for hare in range(1, len(nums)):

            # If unique, increment turtle making it increment only when there is unique value
            if nums[hare] != nums[hare - 1]:
                nums[turtle] = nums[hare]
                turtle += 1

        return turtle