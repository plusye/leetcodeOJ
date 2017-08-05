#!/usr/bin/env python3.5

class Solution:
    def twoSum(self, nums, target):
    	copy_nums = {}
    	for key, value in enumerate(nums):
    		if target - value in copy_nums:
    			return [copy_nums[target - value], key]
    		copy_nums[value] = key
    		

solution = Solution()
result = solution.twoSum([3, 2, 4], 6)
print(result)