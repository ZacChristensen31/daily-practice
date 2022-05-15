from typing import List

"""
Binary Search Algorithm

inputs:
    nums: sorted list of integers
    target: integer to search for
    
outputs:
    index of target in nums, or -1 if target is not in nums
"""


def binary_search(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
