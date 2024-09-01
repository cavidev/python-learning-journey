from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for num in nums:
        for index, x in enumerate(nums):
            if index == 0:
                continue
            if num + nums[index] == target:
                return [num, nums[index]]


print(twoSum([2, 7, 11, 15], 9))

print(twoSum([3, 2, 4], 6))

print(twoSum([3, 3], 6))
