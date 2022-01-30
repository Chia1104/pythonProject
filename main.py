from typing import List


# Tortoise and Hare Algorithm
def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1


# LeetCode Q1
def twoSum(nums: List[int], target: int) -> List[int]:
    initMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in initMap:
            return [initMap[diff], i]
        initMap[n] = i
    return


print(twoSum([2, 7, 11, 15], 18))
