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

    def tashizanKun(self, nums: List[int], target: int) -> List[int]:
        # Write your solution here
        n_dict = {}
        ans_list = []
        for n in range(len(nums)):
            n_dict[nums[n]] = n
        
        c_dict = n_dict.copy()

        for num,index in n_dict.items():
            num2 = target - num
            if num2 in c_dict and num != num2:
                ans_list.append([index,n_dict[num2]])
                del c_dict[num]
                
        return ans_list


def main():
    print(Solution().tashizanKun([2, 7, 11, 15], 9))

    # more test cases
    # print(Solution().tashizanKun([4, 5, 1, 8], 6))  expected answer [1, 2]
    # print(Solution().tashizanKun([0, 7, 9, 4, 5, 1, 8], 5))  expected answer [0, 4]
    # print(Solution().tashizanKun([3, -4, 8, 11]], 7))  expected answer [1, 3]
    # print(Solution().tashizanKun([0, -1, 2, -6, 8, -5, 18]], 12))  expected answer [3, 6]


if __name__ == '__main__':
    main()
