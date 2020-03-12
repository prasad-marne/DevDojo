"""
Two sums:
Given an array of integers, return indices of the two numbers such that they add up to a target number.

[reference] (https://leetcode.com/problems/two-sum/)
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
from typing import List


class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Write your solution here
        return [0, 0]


def main():
    print(Solution().twoSum([2, 7, 11, 15], 9))

    # more test cases
    # print(Solution().twoSum([4, 5, 1, 8], 6))  expected answer [1, 2]
    # print(Solution().twoSum([0, 7, 9, 4, 5, 1, 8], 5))  expected answer [0, 4]
    # print(Solution().twoSum([3, -4, 8, 11]], 7))  expected answer [1, 3]
    # print(Solution().twoSum([0, -1, 2, -6, 8, -5, 18]], 12))  expected answer [3, 6]


if __name__ == '__main__':
    main()
