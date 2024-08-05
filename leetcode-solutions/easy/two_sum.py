"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

# link: https://leetcode.com/problems/two-sum/submissions/1345128665/

# test case

# nums = [2, 7, 11, 15]
# target = 9
nums = [3, 2, 4]
target = 6
# nums = [3, 3]
# target = 6


class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            num_map[num] = i
        index_target = []
        for i, num in enumerate(nums):
            diffr = target - num
            if diffr in num_map and num_map[diffr] != i:
                index_target.append(i)
                index_target.append(num_map[diffr])
                break
        return index_target


solution = Solution()
print(solution.twoSum(nums=nums, target=target))
