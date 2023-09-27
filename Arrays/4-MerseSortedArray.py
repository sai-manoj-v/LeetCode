# Merge sort to merge two sorted array with O(m+n)
def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
    secondIndex = 0
    for i in range(0, len(nums1)):
        while (secondIndex < n) and (nums1[i] > nums2[secondIndex]):
            nums1.insert(i, nums2[secondIndex])
            secondIndex += 1
    nums1[m+secondIndex:] = nums2[secondIndex:]
    return nums1
